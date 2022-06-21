# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class CustomerInvoiceInfo(models.TransientModel):
    _name = "customer.invoice.report.wizard"
    _description = "Invoice Customer Report wizard"

    date_from = fields.Date(string='Date from', required=True)
    date_to = fields.Date(string='Date to', required=True)

    def check_report(self):
        data = {}
        data['form'] = self.read(['date_from', 'date_to'])[0]
        return self._print_report(data)

    def _print_report(self, data):
        data['form'].update(self.read(['date_from', 'date_to'])[0])
        return self.env.ref('de_invoice_tag_wise_report.invoice_customer_report_action').report_action(self, data=data,
                                                                                                      config=False)