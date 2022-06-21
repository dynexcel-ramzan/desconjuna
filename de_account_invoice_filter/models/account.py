from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    c_agent_id = fields.Many2one(related='partner_id.agent_id', string='Agent', store=True, readonly=True)
