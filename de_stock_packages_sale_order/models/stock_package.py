from odoo import models,fields,api,_
from odoo.exceptions import Warning

class StockPackage(models.Model):
    _inherit = 'stock.quant.package'

    sale_order = fields.Char(string='Sale Order')
