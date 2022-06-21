# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons import decimal_precision as dp

class Product(models.Model):
    _inherit = 'product.template'

    product_width = fields.Float(string='Product Width')


class Product(models.Model):
    _inherit = 'product.product'
    
    product_width = fields.Float(related='product_tmpl_id.product_width', string='Prodct Width', store=True, readonly=True)


class Product(models.Model):
    _inherit = 'account.move.line'

    product_width = fields.Float(related='product_id.product_width', string='Prdct Width', store=True,
                                readonly=True)