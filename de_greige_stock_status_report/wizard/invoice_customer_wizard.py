# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class GreigeStockInfo(models.TransientModel):
    _name = "greige.stock.report.wizard"
    _description = "Greige Stock Status Report wizard"

#     date_from = fields.Datetime(string='Date From', required=True)
#     date_to = fields.Datetime(string='Date To', required=True)
    from_lot_id = fields.Many2one('stock.production.lot', string="From Lot Number")
    to_lot_id = fields.Many2one('stock.production.lot', string="To Lot Number")
    owner_ids = fields.Many2many('res.partner', string="Owner")
    zero_balance = fields.Boolean(string="Zero Balance")
    negative_balance = fields.Boolean(string="Negative Balance")
    def check_report(self):
        data = {}
        data['form'] = self.read(['from_lot_id', 'to_lot_id'])[0]
        return self._print_report(data)

    def _print_report(self, data):
        data['form'].update(self.read(['from_lot_id', 'to_lot_id'])[0])
        return self.env.ref('de_greige_stock_status_report.greige_stock_report_action').report_action(self, data=data,
                                                                                                      config=False)