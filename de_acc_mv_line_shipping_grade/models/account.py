from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    shipping_grade = fields.Selection(related='package_id.shipping_grade', string='Grade', store=True, readonly=True)
