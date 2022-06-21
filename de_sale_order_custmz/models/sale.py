from datetime import datetime
from odoo import models,fields,api
from odoo.exceptions import Warning

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    greige_width = fields.Float(string="Greige Width")
    required_gsm = fields.Float(string="Req GSM(g)")
    sinjing = fields.Selection(string="Sinjing",
                               selection=[('y', 'Yes'), ('n', 'No')])
    packing = fields.Selection(string="Packing",
                                      selection=[('bale', 'Bale'), ('rolls', 'Rolls'), ('pcs', 'Pcs')])
    packing_material = fields.Selection(string="Packing Material",
                               selection=[('s.fold', 'S.fold'), ('d.fold', 'D.fold'), ('s.taat', 'S.taat'),
                                          ('d.taat', 'D.taat'), ('plastic', 'Plastic')])


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    greige_width = fields.Float(string="Greige Width")
    required_gsm = fields.Float(string="Req GSM(g)")
