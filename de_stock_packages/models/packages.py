from datetime import datetime
from odoo import models,fields,api
from odoo.exceptions import Warning

class QuantPackages(models.Model):
    _inherit = 'stock.quant.package'

    shipping_quantity = fields.Float('Shipping Quantity')
    shipping_grade = fields.Selection(string="Grade",
                                      selection=[('fresh', 'Fresh'), ('b', 'B-Grade'), ('c', 'Cut Piece')])
