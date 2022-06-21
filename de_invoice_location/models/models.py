# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    
    location_id = fields.Many2one('stock.location', 'Grd. Location', required=False)

