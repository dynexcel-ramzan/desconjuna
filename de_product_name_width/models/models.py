# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons import decimal_precision as dp

class Product(models.Model):
    _inherit = 'product.template'

    product_width = fields.Float(string='Product Width')