from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'mrp.production'

    # @api.multi
    def action_back_to_draft(self):
        self.write({'state': 'confirmed'})
        moves = self.mapped('move_raw_ids')
        moves.action_back_to_draft()


