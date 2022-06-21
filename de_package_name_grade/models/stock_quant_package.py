# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

        
class MaintenanceEquipment(models.Model):
    _inherit = 'stock.quant.package'

    # @api.multi
    def name_get(self):
        result = []
        for record in self:
            if record.shipping_grade:
                result.append((record.id, str(record.name) + ' / ' + str(dict(record._fields['shipping_grade'].selection).get(record.shipping_grade))))
            else:
                result.append((record.id, record.name))
        return result

    

    
