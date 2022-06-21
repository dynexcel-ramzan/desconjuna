from odoo import api, fields, models
from odoo.exceptions import UserError


class PurchaseOrderEnhancement(models.Model):
    _inherit = 'stock.picking.type'

    name = fields.Char(string="Name")