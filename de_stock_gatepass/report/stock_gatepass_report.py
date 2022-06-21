from odoo import tools
from odoo import api, fields, models


class StockGatePassReport(models.Model):
    _name = "stock.gatepass.report"
    _description = "Gatepass Analysis Report"
    _auto = False
    _rec_name = 'date'
    _order = 'date desc'

    @api.model
    def _get_done_states(self):
        return ['processed', 'done']

    name = fields.Char('Reference', readonly=True)
    date = fields.Datetime('Schedule Date', readonly=True)
    product_id = fields.Many2one('product.product', 'Product', readonly=True)
    driver_name = fields.Char(string='Driver', readonly=True)
    vehicle_no = fields.Char(string='Vehicle', readonly=True)
    manual_number = fields.Char(string='Manual Gatepass Number', readonly=True)
    delivery_order = fields.Many2one('stock.picking', readonly=True)
    # product_uom = fields.Many2one('uom.uom', 'Unit of Measure', readonly=True)
    lot_number = fields.Many2one('stock.production.lot', 'Lot Number', readonly=True)
    owner = fields.Many2one('res.partner', 'Owner', readonly=True)
    quantity_done = fields.Float(string="Quantity Done", readonly=True)
    previous_gatepass_quantity = fields.Float(string="Previous Gatepass Qty", readonly=True)
    gatepass_quantity = fields.Float('Gatepass Quantity', readonly=True)
    # move_line_id = fields.Many2one('stock.move.line', invisible=True)
    remaining_quantity = fields.Float('Remaining Quantity', readonly=True)
    nbr = fields.Integer('# of Lines', readonly=True)
    state = fields.Selection([('draft', 'Draft'),
                              ('processed', 'Process'),
                              ('done', 'Done'),
                              ('cancel', 'Cancelled')], string="Status", readonly=True)
    package_id = fields.Many2one('stock.quant.package', string="Source Package", readonly=True)
    gatepass_id = fields.Many2one('stock.gatepass', 'GP#', readonly=True)
    partner_id = fields.Many2one('res.partner', string='Partner', readonly=True)
    sale_order = fields.Char(string='Sale Order', readonly=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        with_ = ("WITH %s" % with_clause) if with_clause else ""

        select_ = """
            min(l.id) as id,
            l.product_id as product_id,
            sum(l.quantity_done) as quantity_done,
            sum(l.previous_gatepass_quantity) as previous_gatepass_quantity,
            sum(l.gatepass_quantity) as gatepass_quantity,
            sum(l.quantity_done - l.previous_gatepass_quantity) as remaining_quantity,
            l.owner as owner,
            l.package_id as package_id,
            l.lot_number as lot_number,
            count(*) as nbr,
            s.name as name,
            s.driver_name as driver_name,
            s.vehicle_no as vehicle_no,
            s.manual_number as manual_number,
            s.delivery_order as delivery_order,
            s.scheduled_date as date,
            s.state as state,
            s.partner_id as partner_id,
            s.sale_order as sale_order,
            s.id as gatepass_id
        """

        for field in fields.values():
            select_ += field

        from_ = """
                stock_gatepass_line l
                      join stock_gatepass s on (l.gatepass_id=s.id)
                      join res_partner partner on s.partner_id = partner.id
                        left join product_product p on (l.product_id=p.id)
                %s
        """ % from_clause

        groupby_ = """
            l.product_id,
            l.gatepass_id,
            l.package_id,
            l.lot_number,
            s.name,
            s.driver_name,
            s.vehicle_no,
            s.manual_number,
            s.delivery_order,
            s.scheduled_date,
            s.partner_id,
            s.sale_order,
            l.owner,
            s.state,
            s.id %s
        """ % (groupby)

        return '%s (SELECT %s FROM %s WHERE l.product_id IS NOT NULL GROUP BY %s)' % (with_, select_, from_, groupby_)

    # @api.model_cr
    def init(self):
        # self._table = sale_report
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (%s)""" % (self._table, self._query()))