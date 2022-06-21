from odoo import models, fields, api
from datetime import datetime

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    production_date = fields.Datetime(string="Production Date")


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    production_date = fields.Datetime(string="Production Date")


class StockMove(models.Model):
    _inherit = 'stock.move'

    production_date = fields.Datetime(string="Production Date")