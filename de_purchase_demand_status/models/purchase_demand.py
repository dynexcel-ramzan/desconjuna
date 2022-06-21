from odoo import models, fields, api


class PurchaseOrderMultiple(models.Model):
    _inherit = 'purchase.order.multiple'

    purchase_count = fields.Integer(string="Purchase", compute='get_purchase_count')
    state = fields.Selection([
        ('draft', 'RFQ'),
        ('po-created', 'PO Created'),
    ], string='Status', compute='action_state', readonly=True, copy=False, index=True)

    # @api.multi
    def action_state(self):
        for rec in self:
            if rec.po_created == 1:
                rec.state = 'po-created'
            else:
                rec.state = 'draft'

    def action_view_test(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'binding_type': 'object',
            'domain': [('origin', '=', self.name)],
            'multi': False,
            'name': 'Purchase',
            'target': 'current',
            'res_model': 'purchase.order',
            'view_mode': 'tree,form',
        }

    def get_purchase_count(self):
        for rec in self:
            count = self.env['purchase.order'].search_count([('origin', '=', self.name)])
            rec.purchase_count = count

