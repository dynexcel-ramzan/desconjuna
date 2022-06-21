# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    cloth_desciption = fields.Text(related='lot_id.cloth_desc')
    # value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
