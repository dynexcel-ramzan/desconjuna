# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from . import config
from . import update

from collections import defaultdict
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.osv import expression


class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _prepare_mo_vals(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values,
                         bom):
        #         config.list12.append(origin)
        date_planned = self._get_date_planned(product_id, company_id, values)
        date_deadline = values.get('date_deadline') or date_planned + relativedelta(
            days=company_id.manufacturing_lead) + relativedelta(days=product_id.produce_delay)
        mo_values = {
            'origin': origin,
            'product_id': product_id.id,
            #             'sale_id': origin,
            'product_description_variants': values.get('product_description_variants'),
            'product_qty': product_qty,
            'product_uom_id': product_uom.id,
            'location_src_id': self.location_src_id.id or self.picking_type_id.default_location_src_id.id or location_id.id,
            'location_dest_id': location_id.id,
            'bom_id': bom.id,
            'date_deadline': date_deadline,
            'date_planned_start': date_planned,
            'procurement_group_id': False,
            'propagate_cancel': self.propagate_cancel,
            'orderpoint_id': values.get('orderpoint_id', False) and values.get('orderpoint_id').id,
            'picking_type_id': self.picking_type_id.id or values['warehouse_id'].manu_type_id.id,
            'company_id': company_id.id,
            'move_dest_ids': values.get('move_dest_ids') and [(4, x.id) for x in values['move_dest_ids']] or False,
            'user_id': False,
        }
        # Use the procurement group created in _run_pull mrp override
        # Preserve the origin from the original stock move, if available
        if location_id.get_warehouse().manufacture_steps == 'pbm_sam' and values.get('move_dest_ids') and values.get(
                'group_id') and values['move_dest_ids'][0].origin != values['group_id'].name:
            origin = values['move_dest_ids'][0].origin
            config.list12.append(origin)
            mo_values.update({
                'name': values['group_id'].name,
                'procurement_group_id': values['group_id'].id,
                'origin': origin,
                'sale_id': config.list12[0],
            })
        return mo_values


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    sale_id = fields.Char(string='Ref Sale')


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    sale_ref_id = fields.Char(string='Ref Sale')


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    sale_tag = fields.Many2one('sale.order', string="Sale Tag")
    sale_ref = fields.Char(string='Ref Sale')
    mo_product_id = fields.Many2one('product.product', string="MO Product")


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # @api.multi
    def action_confirm(self):
        config.list12 = []
        res = super(SaleOrder, self).action_confirm()

        return res
