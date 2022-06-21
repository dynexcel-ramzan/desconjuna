from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    sale_person = fields.Many2one(related='partner_id.sale_person', string="Saleperson", store=True)
