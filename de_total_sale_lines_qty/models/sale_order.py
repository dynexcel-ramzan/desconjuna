from odoo import models, fields, api


class TotalOrderLineQty(models.Model):
    _inherit = 'sale.order'

    tot_order_qty = fields.Float(compute='_calculate_tot_order_qty', string='Total Order Qty',
                                help="Total order quantity in active document")
    tot_delivered_qty = fields.Float(compute='_calculate_tot_delivered_qty', string='Total Delivered Qty',
                                help="Total delivered quantity in active document")
    tot_invoiced_qty = fields.Float(compute='_calculate_tot_invoiced_qty', string='Total Invoiced Qty',
                                help="Total invoiced quantity in active document")

    def _calculate_tot_order_qty(self):
        for rs in self:
            tot_qty = 0
            for line in rs.order_line:
                tot_qty += line.product_uom_qty
            rs.tot_order_qty = tot_qty

    def _calculate_tot_delivered_qty(self):
        for rs in self:
            tot_qty = 0
            for line in rs.order_line:
                tot_qty += line.qty_delivered
            rs.tot_delivered_qty = tot_qty

    def _calculate_tot_invoiced_qty(self):
        for rs in self:
            tot_qty = 0
            for line in rs.order_line:
                tot_qty += line.qty_invoiced
            rs.tot_invoiced_qty = tot_qty
