# -*- coding: utf-8 -*-

#from odoo import models, fields, api, _
        
#class MaintenanceEquipment(models.Model):
 #   _inherit = 'maintenance.equipment'
#
 #   @api.multi
  #
  #def name_get(self):
   #     result = []
    #    for record in self:
    #        if record.equipment_id:
   #             result.append((record.id, record.name + ' / ' + record.equipment_id.name))
   #         else:
    #            result.append((record.id, record.name))
                
     #   return result


#class MaintenanceRequest(models.Model):
 #   _inherit = 'maintenance.request'
    
  #  equip_parent_id = fields.Many2one('maintenance.equipment.category', related='equipment_id.category_id', string='Parent Equipment',  readonly=True)    



#class MaintenanceOrder(models.Model):
 #   _inherit = 'maintenance.order'
    
  #  equip_parent_id = fields.Many2one('maintenance.equipment.category', related='equipment_id.category_id', string='Parent Equipment', readonly=True)
