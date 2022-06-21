# Copyright 2019 Eficent Business and IT Consulting Services, S.L.
# Copyright 2019 Aleph Objects, Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class StockInventory(models.Model):
    _inherit = 'stock.inventory'

    force_inventory_date = fields.Boolean(
        help="Force the inventory moves and accounting entries to a given date"
             "in the past.",
        readonly=True,
        states={'draft': [('readonly', False)]},
    )

    @api.onchange('date')
    def _onchange_force_inventory_date(self):
        if self.force_inventory_date:
            self.accounting_date = self.date.date()

    # @api.multi
    def write(self, vals):
        """For inventories with `force_inventory_date` we only allow to
        change `date` if they are in draft and not being confirmed."""
        force_date = self.filtered(lambda l: l.force_inventory_date)
        if not force_date or not vals.get('date'):
            return super().write(vals)
        res = super(StockInventory, self - force_date).write(vals)
        if vals.get('state'):
            vals.pop('date')
            res &= super(StockInventory, force_date).write(vals)
        else:
            draft = force_date.filtered(lambda i: i.state == 'draft')
            res &= super(StockInventory, draft).write(vals)
            vals.pop('date')
            res &= super(StockInventory, force_date - draft).write(vals)
        return res

    # @api.multi
    def _get_inventory_lines_values(self):
        """Return the values of the inventory lines to create for this inventory.

        :return: a list containing the `stock.inventory.line` values to create
        :rtype: list
        """
        self.ensure_one()
        quants_groups = self._get_quantities()
        vals = []
        for (product_id, location_id, lot_id, package_id, owner_id), quantity in quants_groups.items():
            line_values = {
                'inventory_id': self.id,
                'product_qty': 0 if self.prefill_counted_quantity == "zero" else quantity,
                'theoretical_qty': quantity,
                'prod_lot_id': lot_id,
                'partner_id': owner_id,
                'product_id': product_id,
                'location_id': location_id,
                'package_id': package_id
            }
            line_values['product_uom_id'] = self.env['product.product'].browse(product_id).uom_id.id
            vals.append(line_values)
        if self.exhausted:
            vals += self._get_exhausted_inventory_lines_vals({(l['product_id'], l['location_id']) for l in vals})
        return vals

    # @api.multi
    def post_inventory(self):
        forced_inventories = self.filtered(
            lambda inventory: inventory.force_inventory_date)
        for inventory in forced_inventories:
            lock_date = fields.Date.from_string(
                inventory.company_id.force_inventory_lock_date)
            inventory_date = fields.Datetime.from_string(inventory.date).date()
            if lock_date and inventory_date < lock_date:
                raise ValidationError(_(
                    'It is not possible to force an inventory adjustment to '
                    'a date before %s') % lock_date)
            super(StockInventory, inventory.with_context(
                forced_inventory_date=inventory.date)).post_inventory()
        other_inventories = self - forced_inventories
        if other_inventories:
            super(StockInventory, other_inventories).post_inventory()
