# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class PickingTypeOwner(models.Model):
    _inherit = 'stock.picking.type'

    is_owner = fields.Boolean(string='Assign Owner',default=False)
    
class PickingOwner(models.Model):
    _inherit = 'stock.picking'
    
    assigned_owner = fields.Boolean(string='Assign Owner',default=False)

    @api.multi
    def write(self):
        self.ensure_one()
        if self.state in ('confirmed','assigned'):
            if self.picking_type_id.is_owner and not(self.assigned_owner):
                raise UserError(_('Owner is not assigned'))
            else:
                res = super(PickingOwner, self).write()
        else:
            res = super(PickingOwner, self).wrtie()
    
    @api.multi
    def button_validate1(self):
        for rs in self:
            if rs.picking_type_id.is_owner:
                if not(rs.owner_id) or not(rs.assigned_owner):
                    raise UserError(_('Owner is not assigned'))
                else:
                    res = super(PickingOwner, self).button_validate()
            else:
                res = super(PickingOwner, self).button_validate()
        
                
    @api.one
    def action_assign_owner(self):
        self.assigned_owner = True
        res = super(PickingOwner, self).action_assign_owner()