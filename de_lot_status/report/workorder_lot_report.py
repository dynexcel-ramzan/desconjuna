# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import tools
from odoo import api, fields, models


class StockMoveLotReport(models.Model):
    _name = "report.stock.move.lot"
    _description = "Stock Move Lot Report"
    _auto = False
    _rec_name = 'date'
    _order = 'date desc'
    
    #name = fields.Char('Reference', readonly=True)
    date = fields.Datetime('Date', readonly=True)
    
    partner_id = fields.Many2one('res.partner', 'Partner', readonly=True)
    location_id = fields.Many2one('stock.location', 'Location', readonly=True)
    lot_name = fields.Char('Lot', readonly=True)
    product_id = fields.Many2one('product.product', 'Product', readonly=True)
    package_id = fields.Many2one('stock.quant.package', 'Package', readonly=True)
    qty_done = fields.Float('Quantity', readonly=True)    
        
    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        with_ = ("WITH %s" % with_clause) if with_clause else ""

        select_ = """
        count(a.*) as nbr, min(a.id) as id, max(a.date) as date, a.partner_id, a.lot_name, max(a.product_id) as product_id, a.location_id, a.package_id, sum(a.qty_done) as qty_done from (
select m.date, m.id, lot.name as lot_name, l.product_id, sl.id as location_id, lot.partner_id, l.result_package_id as package_id, l.qty_done
from stock_move m
join stock_move_line l on l.move_id = m.id
join stock_location sl on l.location_dest_id = sl.id
join stock_production_lot lot on l.lot_id = lot.id
left join stock_quant_package pk on l.result_package_id = pk.id
where sl.usage = 'internal'
union
select m.date, m.id, lot.name as lot_name, l.product_id, sl.id as location_id, lot.partner_id, l.result_package_id as package_id, l.qty_done*-1 as qty_done
from stock_move m
join stock_move_line l on l.move_id = m.id
join stock_location sl on l.location_id = sl.id
join stock_production_lot lot on l.lot_id = lot.id
left join stock_quant_package pk on l.package_id = pk.id
where sl.usage = 'internal'
) a
group by a.partner_id, a.lot_name, a.location_id, a.package_id
        
        """

        for field in fields.values():
            select_ += field
        
        from_ = groupby_ = ''

        return '%s (SELECT %s %s %s)' % (with_, select_, from_, groupby_)

    # @api.model_cr
    def init(self):
        # self._table = sale_report
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (%s)""" % (self._table, self._query()))