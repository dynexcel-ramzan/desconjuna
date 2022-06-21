from odoo import api, fields, models, _
from odoo.exceptions import UserError


class StockMoveWizard(models.Model):
    _name = "stock.transfer.wizard"
    _description = "Daily Stitch Wizard"

    from_date = fields.Datetime(string='From Date')
    to_date = fields.Datetime(string='To Date')
    
    def print_production_pdf(self):
        data = {}
        data['form'] = self.read(['from_date'])[0]
        data['form'] = self.read(['to_date'])[0]
        return self.env.ref('de_daily_stitched_report.production_report').report_action(self, data=data, config=False)