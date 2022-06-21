# -*- coding: utf-8 -*-

from odoo import models, fields, api



class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    
    package_id = fields.Many2one('stock.quant.package', string='Package', store=True, required=False)
    shipping_quantity_r = fields.Float(related='package_id.shipping_quantity')
