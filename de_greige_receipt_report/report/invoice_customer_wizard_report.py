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


class GreigeReceiptReport(models.AbstractModel):
    _name = 'report.de_greige_receipt_report.greige_receipt_report_pdf'
    _description = 'Greige Receipt information'

    def _get_report_values(self, docids, data=None):
        model = self.env.context.get('active_model')
        docs = self.env['greige.receipt.report.wizard'].browse(self.env.context.get('active_id'))
        invoice_ids = ''
        date_from = docs.date_from
        date_to = docs.date_to
#         owner_ids = docs.owner_ids
        stock_ids = self.env['stock.move.line'].search([('date', '>=', date_from), ('date', '<=', date_to), ('location_id.id','=', 9), ('location_dest_id.id','=', 20), ('state','=', 'done')])

        return {
            'docs': docs,
            'date_from': date_from,
            'date_to': date_to,
#             'owner_ids': owner_ids,
            'stock_ids': stock_ids,
        }