# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
        
class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            if record.category_id:
                result.append((record.id, record.name + ' / ' + record.category_id.name))
            else:
                result.append((record.id, record.name))
                
        return result
