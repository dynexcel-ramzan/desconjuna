from odoo import models, fields, api


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    tot_consume_qty = fields.Float(string='Consumed Qty', compute='_get_consumed_qty',
                                 help="Total Consumed quantity in active document", store=True, readonly=True)

    @api.depends('move_raw_ids', 'move_raw_ids.quantity_done')
    def _get_consumed_qty(self):
        for rec in self:
            tot_cons_qty = 0
            for line in rec.move_raw_ids:
                tot_cons_qty += line.quantity_done
            rec.tot_consume_qty = tot_cons_qty