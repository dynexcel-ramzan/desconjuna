# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'
    
    location_id = fields.Many2one('stock.location', 'Grd. Location', required=False)

