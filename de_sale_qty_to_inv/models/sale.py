from odoo import models, fields, api


class TotalInvQty(models.Model):
    _inherit = 'sale.order'

    qty_to_inv = fields.Float(compute='_calculate_qty_to_inv', string='Qty To Invoice',
                                help="Quantity To Invoice in active document")

    def _calculate_qty_to_inv(self):
        for rs in self:
            tot_sale_qty = 0
            tot_delivered_qty = 0
            tot_invoiced_qty = 0
            qty_inv = 0
            for line in rs.order_line:
                tot_sale_qty += line.product_uom_qty
                tot_delivered_qty += line.qty_delivered
                tot_invoiced_qty += line.qty_invoiced
                qty_inv = tot_delivered_qty - tot_invoiced_qty
            rs.qty_to_inv = qty_inv
