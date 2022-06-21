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


class InvoiceReport(models.AbstractModel):
    _name = 'report.de_customer_invoice_report.invoice_report_customer'
    _description = 'Monthly Processing Report'

    def _get_report_values(self, docids, data=None):
        model = self.env.context.get('active_model')
        docs = self.env['account.invoice.wizard'].browse(self.env.context.get('active_id'))
        invoice_ids = ''
        date_from = docs.date_from
        date_to = docs.date_to
        invoice_ids = self.env['account.move'].search([('invoice_date', '>=', date_from), ('invoice_date', '<=', date_to), ('move_type','=', 'out_invoice')])

        return {
            'docs': docs,
            'date_from': date_from,
            'date_to': date_to,
            'invoice_ids': invoice_ids,
        }