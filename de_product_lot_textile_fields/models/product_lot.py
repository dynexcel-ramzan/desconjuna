from datetime import datetime
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class ProductLot(models.Model):
    _inherit = 'stock.production.lot'

    cloth_type_id = fields.Many2one('product.cloth.type', string='Cloth Type', help="Greige or Cloth Yarn Type")
    ratio = fields.Char('Ratio')
    reed = fields.Integer('Reed')
    pick = fields.Integer('Pick')
    warp = fields.Integer('Warp')
    weft = fields.Integer('Weft')
    wd = fields.Float('Width')
    cloth_desc = fields.Text(string='Cloth Desc.', compute='_compute_cloth_description')
    # cloth_desc = fields.Text(string='Cloth Desc.')
    cloth_type_active = fields.Boolean(string='Active',readonly=True,default=False)
    cloth_type_active = fields.Boolean(related='product_id.is_greige_type', string='Active', store=True)
    is_lot_move = fields.Boolean(string='Has Movement',compute='_compute_product_movement')
    
    # @api.multi
    # @api.depends('cloth_type_id', 'reed', 'pick', 'warp', 'weft', 'wd')
    def _compute_cloth_description(self):
        ratio = ""
        for rs in self:
            if rs.cloth_type_id:
                if rs.ratio:
                    ratio = rs.ratio + " "
                else:
                    ratio = ""
                rs.cloth_desc = rs.cloth_type_id.name + " " + ratio + str(rs.reed) + "x" + str(rs.pick) + "/" + str(rs.warp) + "x" + str(rs.weft) + " " + str(rs.wd) + '"'
            else:
                rs.cloth_desc = ' '
                
    # @api.multi
    def _compute_product_movement(self):
        for rs in self:
            has_moves = self.env['stock.move.line'].search([('product_id', '=', rs.product_id.id), ('lot_id', '=', rs.id)])
            if has_moves:
                rs.is_lot_move = True
            else:
                rs.is_lot_move = False
     
class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_greige_type = fields.Boolean(string="Is Greige", default=False)
    
class ProductClothType(models.Model):
    _name = 'product.cloth.type'
    _description = 'Product Cloth Type'
    
    name = fields.Text(string='Cloth Type', required=True)

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'
    
    is_greige_type = fields.Boolean(related='product_id.is_greige_type', string='Active', store=True)
    cloth_desc = fields.Text(related='lot_id.cloth_desc', string='Cloth Desc.', store=True)