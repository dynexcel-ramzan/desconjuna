from odoo import models, fields, api


class TotalOrderLineQty(models.Model):
    _inherit = 'purchase.order'

    tot_order_qty = fields.Float(compute='_calculate_tot_order_qty', string='Total Order Qty',
                                help="Total order quantity in active document")
    tot_received_qty = fields.Float(compute='_calculate_tot_delivered_qty', string='Total Received Qty',
                                help="Total received quantity in active document")
    tot_bill_qty = fields.Float(compute='_calculate_tot_invoiced_qty', string='Total Billed Qty',
                                help="Total Billed quantity in active document")

    def _calculate_tot_order_qty(self):
        for rs in self:
            tot_qty = 0
            for line in rs.order_line:
                tot_qty += line.product_qty
            rs.tot_order_qty = tot_qty

    def _calculate_tot_delivered_qty(self):
        for rs in self:
            tot_qty = 0
            for line in rs.order_line:
                tot_qty += line.qty_received
            rs.tot_received_qty = tot_qty

    def _calculate_tot_invoiced_qty(self):
        for rs in self:
            tot_qty = 0
            for line in rs.order_line:
                tot_qty += line.qty_invoiced
            rs.tot_bill_qty = tot_qty
