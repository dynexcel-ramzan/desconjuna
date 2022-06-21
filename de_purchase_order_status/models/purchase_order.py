from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    purchase_status = fields.Selection([
        ('draft', 'Draft'), ('pending', 'Pending'),
        ('partially-receive', 'Partially Recieved'),
        ('fully-receive', 'Fully Recieved'),
        ('no-bill', 'No Bill'),
        ('partially-bill', 'Partially Billed'),
        ('fully-bill', 'Fully Bill'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Purchase Status')


