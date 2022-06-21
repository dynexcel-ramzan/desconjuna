# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class InvoiceInfo(models.TransientModel):
    _name = "account.invoice.wizard"
    _description = "Monthly Processing Report wizard"

    date_from = fields.Date(string='Date from', required=True)
    date_to = fields.Date(string='Date to', required=True)

    def check_report(self):
        data = {}
        data['form'] = self.read(['date_from', 'date_to'])[0]
        return self._print_report(data)

    def _print_report(self, data):
        data['form'].update(self.read(['date_from', 'date_to'])[0])
        return self.env.ref('de_customer_invoice_report.customer_invoice_report_action').report_action(self, data=data,
                                                                                                      config=False)