from odoo.exceptions import Warning
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class account_move(models.Model):
    _inherit = 'account.move'

    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('approval', 'Waiting for Approval'),
        ('approved', 'Approved'),
        ('posted', 'Posted'),
        ('cancel', 'Cancelled'),
    ], string='Status', required=True, readonly=True, copy=False, tracking=True,
        default='draft')



class account_payment(models.Model):
    _inherit = 'account.payment'

    def mark_as_sent(self):
        self.write({'is_move_sent': True})

    def unmark_as_sent(self):
        self.write({'is_move_sent': False})

    def action_post(self):
        ''' draft -> posted '''
        self.move_id._post(soft=False)

    def action_approval(self):
        ''' draft -> approval '''
        self.write({'state': 'approval'})

    def action_approved(self):
        ''' draft -> approved '''
        return self.action_post()
#         self.write({'state': 'approved'})

    def action_cancel(self):
        ''' draft -> cancelled '''
        self.move_id.button_cancel()

    def action_draft(self):
        ''' posted -> draft '''
        self.move_id.button_draft()
