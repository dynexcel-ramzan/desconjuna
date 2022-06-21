# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, SUPERUSER_ID
from odoo.exceptions import UserError
from datetime import datetime


class Gatepass(models.Model):
    _name = 'stock.gatepass'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Gatepass'

    name = fields.Char(string='Name', copy=False, readonly=True, index=True, default=lambda self: ('New'))
    scheduled_date = fields.Datetime(string='Date', required=True, readonly=True, default=datetime.today(),
                                     states={'draft': [('readonly', False)]})
    driver_name = fields.Char(string='Driver')
    vehicle_no = fields.Char(string='Vehicle')
    manual_number = fields.Char(string='Manual Gatepass Number')
    slip_no = fields.Char(string='Slip Number')
    state = fields.Selection([('draft', 'Draft'),
                              ('processed', 'Process'),
                              ('done', 'Done'),
                              ('cancel', 'Cancelled')], string="Status",
                             default='draft', tracking=True)
    gate_pass_lines = fields.One2many('stock.gatepass.line', 'gatepass_id', string='Move Lines',)
    delivery_order = fields.Many2one('stock.picking', string="Delivery Order", required=False)
    ml_count = fields.Integer(string='Moves',compute='_compute_ml_count')
    partner_id = fields.Many2one(string='Partner', related='delivery_order.partner_id', store=True)
    sale_order = fields.Char(string='Sale Order', related='delivery_order.origin', store=True)

    # @api.onchange('delivery_order')
    # def get_delivery_order_data(self):
    #     for rec in self:
    #         dilvery_oder = rec.env['stock.picking'].search([('name','=', rec.delivery_order.name), ('picking_type_id.id','=', 2)])
    #         rec.update({
    #                 'partner_id': dilvery_oder.partner_id.name,
    #                 'sale_order': dilvery_oder.origin,
    #             })

    def unlink(self):
        if self.state not in ['draft']:
            raise UserError(('Deletion is Not Allowed!'))
        return super(Gatepass, self).unlink()

    @api.onchange('name')
    def onchange_name(self):
        type_id = self.env['stock.picking.type'].search([('code', '=', 'outgoing')]).ids
        picking_id = self.env['stock.picking'].search([('picking_type_id', '=', type_id)]).ids

        return {'domain': {'delivery_order': ['&',('id', 'in', picking_id),('state', '=', 'done')]}}
 
    # @api.multi
    def action_process(self):
        if not self.driver_name and not self.vehicle_no and not self.manual_number:
            raise UserError("Driver Name and Vehicle No and Manual Gatepass number must not be empty,")
        for other_input in self.gate_pass_lines:
            other_input.unlink()
        if self.delivery_order:
            for line in self.delivery_order.move_line_ids_without_package:
                self.env['stock.gatepass.line'].create({
                        'gatepass_id':self.id,
                        'product_id': line.product_id.id,
                        'lot_number': line.lot_id.id,
                        'package_id': line.package_id.id, 
                        'owner': line.owner_id.id,
                        'quantity_done':line.qty_done,
                        'move_line_id': line.id,
                        'previous_gatepass_quantity': line.gatepass_qty
                 })
        self.update({
                 'state': 'processed'
                })   

    @api.model
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('stock.gatepass') or ('New')
        
        delivery_exists = self.search([('delivery_order', '=', vals.get('delivery_order')), ('state', '=', 'draft')])
        if delivery_exists:
            raise UserError('GatePass already in draft for the delivery order!')
        res = super(Gatepass, self).create(vals)
        return res

    def action_confirm(self):
        if self.gate_pass_lines:
            for line in self.gate_pass_lines:
                if line.gatepass_quantity <= 0:
                    raise UserError(('Gatepass Quantity should be greater than 0.'))
                if line.quantity_done > 0:
                    old_qty = line.move_line_id.gatepass_qty
                    line.move_line_id.gatepass_qty = old_qty + line.gatepass_quantity
                    line.move_line_id.gatepass_id = line.gatepass_id.id

        self.state = 'done'

    def _compute_ml_count(self):
        for rec in self:
            ml_data = rec.env['stock.move.line'].search_count([('gatepass_id', '=', self.name)])
            rec.ml_count = ml_data

    def action_view_move_lines(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': ('Move Lines'),
            'res_model': 'stock.move.line',
            'view_mode': 'tree',
            'view_id': self.env.ref('de_stock_gatepass.stock_move_line_tree_view_new', False).id,
            'domain': [('gatepass_id', '=', self.name)],
        }

class StockGatePassLine(models.Model):
    _name = 'stock.gatepass.line'
    _description = 'Gatepass Line'

    gatepass_id = fields.Many2one('stock.gatepass', string='Gatepass', required=False)
    product_id = fields.Many2one('product.product', string="Product")
    package_id = fields.Many2one('stock.quant.package', string="Source Package")
    lot_number = fields.Many2one('stock.production.lot', 'Lot Number')
    owner = fields.Many2one('res.partner', 'Owner')
    quantity_done = fields.Float(string="Quantity Done", store=True)
    previous_gatepass_quantity = fields.Float(string="Previous Gatepass Qty")
    gatepass_quantity = fields.Float('Gatepass Quantity', store=True)
    move_line_id = fields.Many2one('stock.move.line', invisible=True)
    remaining_quantity = fields.Float('Remaining Quantity', compute='compute_remaining_quantity', store=True)
    state = fields.Selection(
        related='gatepass_id.state', string='Gatepass Status', readonly=True, copy=False, store=True, default='draft')
    # state = fields.Selection([('draft', 'Draft'),
    #                           ('processed', 'Process'),
    #                           ('done', 'Done'),
    #                           ('cancel', 'Cancelled')], string="Status",
    #                          default='draft', related='gatepass_id.state', readonly=True)
    # state = fields.Selection([('draft', 'Draft'),
    #                           ('done', 'Done'),
    #                           ('cancel', 'Cancelled')], string="Status", related='gatepass_id.state', readonly=True)

    def compute_remaining_quantity(self):
        for rec in self:
            rec.remaining_quantity = rec.quantity_done - rec.gatepass_quantity

    # make computed field editable using constraints
    @api.constrains('quantity_done', 'previous_gatepass_quantity')
    def _check_gatepass_quantity(self):
        for rec in self:
            if rec.previous_gatepass_quantity > 0:
                rem_gatepass_qty = 0
                rem_gatepass_qty = rec.quantity_done - rec.previous_gatepass_quantity
                rec.update({
                    'gatepass_quantity': rem_gatepass_qty,
                })
    # Inverse Fiunction
    # @api.depends('gatepass_quantity')
    # def _inverse_gatepass_quantity(self):
    #     for rec in self:
    #         # if rec.gatepass_quantity > 0:
    #         rec.gatepass_quantity = rec.gatepass_quantity
    # def _gatepass_quantity(self):
    #     for rec in self:
    #         if rec.gatepass_quantity > 0:
    #             rec.update({
    #                 'gatepass_quantity': rec.gatepass_quantity,
    #             })


    # @api.constrains('gatepass_quantity')
    # def constrains_gatepass_quantity(self):
    #     for rec in self:
    #         if rec.gatepass_quantity <= 0:
    #             raise UserError("Gatepass quantity should be greater than 0")
    #         if rec.gatepass_quantity > (rec.quantity_done - rec.previous_gatepass_quantity):
    #             raise UserError("You can not issue more than quantity done")
