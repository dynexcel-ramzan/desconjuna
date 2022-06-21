# -*- coding: utf-8 -*-

import time
from odoo import api, models, _, fields
from dateutil.parser import parse
from odoo.exceptions import UserError
from datetime import date
from odoo import exceptions
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from datetime import datetime


class CustomerInvoiceReport(models.AbstractModel):
    _name = 'report.de_invoice_tag_wise_report.invoice_customer_report_pdf'
    _description = 'Invoice Customer information'

    def _get_report_values(self, docids, data=None):
        model = self.env.context.get('active_model')
        docs = self.env['customer.invoice.report.wizard'].browse(self.env.context.get('active_id'))
        invoice_ids = ''
        date_from = docs.date_from
        date_to = docs.date_to
        invoice_ids = self.env['account.move'].search([('invoice_date', '>=', date_from), ('invoice_date', '<=', date_to), ('journal_id.id','=', 1)])

        return {
            'docs': docs,
            'date_from': date_from,
            'date_to': date_to,
            'invoice_ids': invoice_ids,
        }