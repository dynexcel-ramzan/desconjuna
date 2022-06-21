from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_status = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('partialy_deliver', 'Partialy Delivered'),
        ('fully_deliver', 'Fully Delivered'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Sale Status')


