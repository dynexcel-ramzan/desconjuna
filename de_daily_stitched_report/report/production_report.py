from odoo.exceptions import UserError
from datetime import datetime
from odoo import api, fields, models, _
from datetime import date, timedelta


class ProductionReportPDF(models.AbstractModel):
    _name = 'report.de_daily_stitched_report.production_report_pdf'
    _description = 'Daily Stitch Production Report'
    
    count = fields.Integer('count')

    def _get_report_values(self, docids, data=None):
        model = self.env.context.get('active_model')
        docs = self.env['stock.transfer.wizard'].browse(self.env.context.get('active_id'))
        stock_ids = ''
        # mrp_ids = ''
        from_date = docs.from_date
        to_date = docs.to_date
        #         date_to = data['form']['date_to']

        #         operation_type = self.env['stock.picking.type'].search([('id', '=', 95)])
        #         raise UserError (operation_type)
        #         if operation_type:
        stock_ids = self.env['stock.move.line'].search([('production_date', '>=', from_date), ('production_date', '<=', to_date), ('product_id.categ_id','=', 237), ('location_dest_id','=', 19)])
        # mrp_ids = self.env['mrp.production'].search([('name', 'in', stock_ids.production_id.name)])
        #         print('stock_ids====',stock_ids

        return {
            'doc_ids': self.ids,
            'docs': docs,
            #             'doc_model': 'hr_attendance.hr.attendance',
            'from_date': docs.from_date,
            'to_date': docs.to_date,
            #             'date_to': data['form']['date_to'],
            'stock_ids': stock_ids,
            # 'mrp_ids': mrp_ids,
        }
