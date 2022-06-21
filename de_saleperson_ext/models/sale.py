from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_person = fields.Many2one(related='partner_id.sale_person', string="Saleperson", store=True)
