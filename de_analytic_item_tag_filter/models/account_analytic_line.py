from odoo import models, fields, api


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    tag = fields.Char(related='move_id.analytic_tag_ids.name', string='Tag', store=True, readonly=True, copy=True)
