from odoo import api, fields, models, _
from odoo.exceptions import UserError


class StockMoveWizard(models.Model):
    _name = "stock.gatepass.transfer.wizard"
    _description = "Gatepass Report"

    from_date = fields.Datetime(string='From Date')
    to_date = fields.Datetime(string='To Date')
    
    def print_gatepass_transfer_pdf(self):
        data = {}
        data['form'] = self.read(['from_date'])[0]
        data['form'] = self.read(['to_date'])[0]
        return self.env.ref('de_gatepass_report.gatepass_report').report_action(self, data=data, config=False)