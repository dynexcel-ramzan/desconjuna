from datetime import datetime
from odoo import models,fields,api
from odoo.exceptions import Warning

class QuantPackage(models.Model):
    _inherit = 'stock.quant.package'

    packing_date = fields.Datetime(string='Package Date')
    packing_quantity = fields.Float(string="Packing Quantity")
    packing_type = fields.Selection(string="Packing",
                                    selection=[('bales', 'Bales'), ('rolls', 'Rolls'), ('thaan', 'Thaan'),
                                               ('sample', 'Sample'), ('w.f', 'W.F')])
