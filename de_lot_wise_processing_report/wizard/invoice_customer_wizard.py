# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class GreigeStockInfo(models.TransientModel):
    _name = "greige.process.report.wizard"
    _description = "Lot Wise Processing wizard"

#     date_from = fields.Datetime(string='Date From', required=True)
#     date_to = fields.Datetime(string='Date To', required=True)
    from_lot_id = fields.Many2one('stock.production.lot', string="From Lot Number")
    to_lot_id = fields.Many2one('stock.production.lot', string="To Lot Number")
    owner_ids = fields.Many2many('res.partner', string="Owner")
    def check_report(self):
        data = {}
        data['form'] = self.read(['from_lot_id', 'to_lot_id'])[0]
        return self._print_report(data)

    def _print_report(self, data):
        data['form'].update(self.read(['from_lot_id', 'to_lot_id'])[0])
        return self.env.ref('de_lot_wise_processing_report.greige_process_report_action').report_action(self, data=data,
                                                                                                      config=False)