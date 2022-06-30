# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

#
# Please note that these reports are not multi-currency !!!
#
import re

from odoo import api, fields, models, tools
from odoo.exceptions import UserError
from odoo.osv.expression import AND, expression


class MaintenanceOrderReport(models.Model):
    _name = "maintenance.order.report"
    _description = "Maintenance Report"
    _auto = False

    #     _rec_name = 'date'
    #     _order = 'date desc'
    @api.model
    def _get_done_states(self):
        return ['confirm', 'inprocess', 'done', 'cancel']

    name = fields.Char('Order Reference', readonly=True)
    schedule_start_date = fields.Date(string='Schedule Start Date', readonly=True)
    schedule_end_date = fields.Date(string='Schedule End Date', readonly=True)
    start_date = fields.Date(string='Start Date', readonly=True, )
    end_date = fields.Date(string='End Date', readonly=True, )
    product_id = fields.Many2one('product.product', 'Product Variant', readonly=True)
    product_uom = fields.Many2one('uom.uom', 'Unit of Measure', readonly=True)
    equipment_id = fields.Many2one('maintenance.equipment', string='Equipment', readonly=True)
    parent_equipment_id = fields.Many2one('maintenance.equipment', string='Parent Equipment', readonly=True)
    analytic_account_id = fields.Many2one('account.analytic.account', 'Analytic Account', readonly=True)
    qty_demand = fields.Float('Dmeand Qty', readonly=True)
    qty_done = fields.Float('Issued Qty', readonly=True)
    company_id = fields.Many2one('res.company', 'Company', readonly=True)
    user_id = fields.Many2one('res.users', 'Responsible', readonly=True)
    currency_id = fields.Many2one('res.currency', 'Currency', readonly=True)
#     price_total = fields.Float('Total', readonly=True)
    price_subtotal = fields.Float('Total', readonly=True)
    price_unit = fields.Float('Cost', readonly=True)
    product_tmpl_id = fields.Many2one('product.template', 'Product', readonly=True)
    categ_id = fields.Many2one('product.category', 'Product Category', readonly=True)
    nbr = fields.Integer('# of Lines', readonly=True)
    analytic_account_id = fields.Many2one('account.analytic.account', 'Analytic Account', readonly=True)
    #     analytic_tag_ids = fields.Many2many('account.analytic.tag', string='Analytic Tags', readonly=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('inprocess', 'Under Maintenance'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ], string='Status', readonly=True)

    order_id = fields.Many2one('maintenance.order', 'Order #', readonly=True)

    def _select_maintenance(self, fields=None):
        if not fields:
            fields = {}
        select_ = """
            min(ml.id) as id,
            ml.product_id as product_id,
            t.uom_id as product_uom,
            CASE WHEN ml.product_id IS NOT NULL THEN sum(ml.demand_qty) ELSE 0 END as qty_demand,
            CASE WHEN ml.product_id IS NOT NULL THEN sum(ml.done_qty) ELSE 0 END as qty_done,
            CASE WHEN ml.product_id IS NOT NULL THEN sum(ml.price_subtotal) ELSE 0 END as price_subtotal,
            count(*) as nbr,
            m.name as name,
            ml.currency_id as currency_id,
            ml.price_unit as price_unit,
            m.schedule_start_date as schedule_start_date,
            m.schedule_end_date as schedule_end_date,
            m.start_date as start_date,
            m.end_date as end_date,
            m.state as state,
            m.user_id as user_id,
            m.company_id as company_id,
            m.equipment_id as equipment_id,
            m.pfiled as parent_equipment_id,
            analytic_account.id as analytic_account_id,
            p.product_tmpl_id as product_tmpl_id,
            t.categ_id as categ_id,
            m.id as order_id
        """

        for field in fields.values():
            select_ += field
        return select_

    def _from_maintenance(self, from_clause=''):
        from_ = """
                maintenance_order_line ml
                      right outer join maintenance_order m on (m.id=ml.maintenance_line)
                        left join product_product p on (ml.product_id=p.id)
                        left join maintenance_equipment me on (m.equipment_id=me.id)
                            left join product_template t on (p.product_tmpl_id=t.id)
                    left join uom_uom u on (u.id=ml.product_uom)
                    left join uom_uom u2 on (u2.id=t.uom_id)
                    left join account_analytic_account analytic_account on (ml.analytic_account_id = analytic_account.id)
                    left join res_currency_rate cr on (cr.currency_id = m.currency_id and
                        cr.company_id = m.company_id)
                    left join {currency_table} ON currency_table.company_id = m.company_id


                %s
        """.format(
            currency_table=self.env['res.currency']._get_query_currency_table(
                {'multi_company': True, 'date': {'date_to': fields.Date.today()}}),
        ) % from_clause
        return from_

    def _group_by_maintenance(self, groupby=''):
        groupby_ = """
            ml.product_id,
            ml.maintenance_line,
            t.uom_id,
            m.name,
            ml.currency_id,
            m.schedule_start_date,
            m.schedule_end_date,
            m.start_date,
            m.end_date,
            ml.price_unit,
            m.user_id,
            m.state,
            p.product_tmpl_id,
            m.pfiled,
            t.categ_id,
            m.company_id,
            analytic_account.id,
            m.id %s
        """ % (groupby)
        return groupby_

    def _query(self, with_clause='', fields=None, groupby='', from_clause=''):
        if not fields:
            fields = {}
        with_ = ("WITH %s" % with_clause) if with_clause else ""
        return '%s (SELECT %s FROM %s WHERE ml.x_display_type IS NULL GROUP BY %s)' % \
               (with_, self._select_maintenance(fields), self._from_maintenance(from_clause),
                self._group_by_maintenance(groupby))

    def init(self):
        #         self._table = maintenance_order_report
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (%s)""" % (self._table, self._query()))
