# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError, Warning

from odoo.addons import decimal_precision as dp
class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'
    
    real_qty = fields.Float('Real Quantity', default=0.0, store=True, compute='_compute_real_quantity', digits=dp.get_precision('Product Unit of Measure'), copy=False)
    
    # @api.multi
    def _compute_real_quantity(self):
        for line in self:
            if line.location_id.usage == 'internal' and line.location_dest_id.usage != 'internal':
                line.real_qty = line.qty_done * -1
            elif line.location_dest_id.usage == 'internal' and line.location_id.usage != 'internal':
                line.real_qty = line.qty_done

