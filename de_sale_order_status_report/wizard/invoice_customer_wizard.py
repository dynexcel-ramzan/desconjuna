# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrderInfo(models.TransientModel):
    _name = "sale.order.status.report.wizard"
    _description = "Sale Order Status Report wizard"

#     date_from = fields.Datetime(string='Date From', required=True)
#     date_to = fields.Datetime(string='Date To', required=True)
    from_sale_order = fields.Many2one('sale.order', string="From SO#")
    to_sale_order = fields.Many2one('sale.order', string="To SO#")
    owner_ids = fields.Many2many('res.partner', string="Owner")
    # zero_balance = fields.Boolean(string="Zero Balance")
    # negative_balance = fields.Boolean(string="Negative Balance")
    def check_report(self):
        data = {}
        data['form'] = self.read(['from_sale_order', 'to_sale_order'])[0]
        return self._print_report(data)

    def _print_report(self, data):
        data['form'].update(self.read(['from_sale_order', 'to_sale_order'])[0])
        return self.env.ref('de_sale_order_status_report.sale_status_report_action').report_action(self, data=data,
                                                                                                      config=False)