# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'
    
    package_id = fields.Many2one('stock.quant.package', 'Package', required=False)

