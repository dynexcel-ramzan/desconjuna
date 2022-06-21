from odoo import models, fields, api

class PurchaseOrderMultiple(models.Model):
    _inherit = 'purchase.order.multiple'

    note = fields.Text(string="Note")
