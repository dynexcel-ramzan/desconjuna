# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class GreigeReceiptInfo(models.TransientModel):
    _name = "greige.receipt.report.wizard"
    _description = "Greige Receipt Report wizard"

    date_from = fields.Datetime(string='Date From', required=True)
    date_to = fields.Datetime(string='Date To', required=True)
    owner_ids = fields.Many2many('res.partner', string="Owner")
    def check_report(self):
        data = {}
        data['form'] = self.read(['date_from', 'date_to'])[0]
        return self._print_report(data)

    def _print_report(self, data):
        data['form'].update(self.read(['date_from', 'date_to'])[0])
        return self.env.ref('de_greige_receipt_report.greige_receipt_report_action').report_action(self, data=data,
                                                                                                      config=False)