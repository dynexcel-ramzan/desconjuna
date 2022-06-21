from odoo import api, fields, models, _
from odoo.exceptions import UserError


class PurchaseOrderWizard(models.Model):
    _name = "stock.transfer.wizard"
    _description = "ST Wizard"

    date_after = fields.Datetime(string='Date After')
    
    def print_production_pdf(self):
        data = {}
        data['form'] = self.read(['date_after'])[0]
        return self.env.ref('de_stock_transfer_report.production_report').report_action(self, data=data, config=False)