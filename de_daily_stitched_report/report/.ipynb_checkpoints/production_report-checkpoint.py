from odoo.exceptions import UserError
from datetime import datetime
from odoo import api, fields, models, _
from datetime import date, timedelta


class ProductionReportPDF(models.AbstractModel):
    _name = 'report.de_stock_transfer_report.production_report_pdf'
    
    count = fields.Integer('count')

    def _get_report_values(self, docids, data=None):
        stock_ids = ''
        date_after = data['form']['date_after']
        #         date_to = data['form']['date_to']

#         operation_type = self.env['stock.picking.type'].search([('id', '=', 95)])
#         raise UserError (operation_type)
#         if operation_type:
        stock_ids = self.env['stock.picking'].search([('picking_type_id.id', '=', 95),('date_done', '>', date_after)])

#         print('stock_ids====',stock_ids)

        return {
            'doc_ids': self.ids,
            #             'doc_model': 'hr_attendance.hr.attendance',
            'date_after': data['form']['date_after'],
            #             'date_to': data['form']['date_to'],
            'stock_ids': stock_ids,
        }
