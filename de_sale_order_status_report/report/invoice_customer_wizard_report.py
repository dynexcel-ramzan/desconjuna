# -*- coding: utf-8 -*-

import time
from odoo import api, models, _, fields
from dateutil.parser import parse
from odoo.exceptions import UserError
from datetime import date
from odoo import exceptions
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from datetime import datetime


class GreigeReceiptReport(models.AbstractModel):
    _name = 'report.de_sale_order_status_report.sale_status_report_pdf'
    _description = 'Sale Order Status information'

    def _get_report_values(self, docids, data=None):
        model = self.env.context.get('active_model')
        docs = self.env['sale.order.status.report.wizard'].browse(self.env.context.get('active_id'))
        from_sale_order = docs.from_sale_order.name
        to_sale_order = docs.to_sale_order.name
        owner_ids = docs.owner_ids.ids
        owner_from_stock_ids = ''
        from_sale_order_ids = ''
        to_sale_order_ids = ''
        from_so_char_1 = ''
        from_so_char_2 = ''
        to_so_char_1 = ''
        to_so_char_2 = ''
        from_so_char = ''
        to_so_char = ''
        from_so_num = ''
        to_so_num = ''
        #       Get From Lot Charachter
        if from_sale_order:
            from_char_count = 0
            for char in from_sale_order:
                from_char_count += 1
                if from_char_count == 1:
                    from_so_char_1 = char
                if from_char_count == 2:
                    from_so_char_2 = char
                    break
            from_so_char = from_so_char_1 + from_so_char_2
            #       End From Sale Charachter
            #       Get From Sale Num
            from_count = 0
            for nchar in from_sale_order:
                from_count += 1
                if from_count > 2:
                    from_so_num += nchar
        #       Get TO Sale Char
        if to_sale_order:
            to_char_count = 0
            for to_char in to_sale_order:
                to_char_count += 1
                if to_char_count == 1:
                    to_so_char_1 = to_char
                if to_char_count == 2:
                    to_so_char_2 = to_char
                    break
            to_so_char = to_so_char_1 + to_so_char_2

            for to_nchar in to_sale_order:
                to_so_char = to_nchar
                break
            #       End To Sale Charachter

            #       Get To Sale NUmber
            to_count = 0
            for to_nchar in to_sale_order:
                to_count += 1
                if to_count > 2:
                    to_so_num += to_nchar

        from_so_num = int(from_so_num) if from_so_num != '' else 0
        to_so_num = int(to_so_num) if to_so_num != '' else 0
        #         raise UserError(str(from_so_num))
        #       End To Sale Number
        so_from_list = self.env['sale.order'].search(
            [('x_sale_reference', '=', from_so_char), ('x_so_number', '>=', int(from_so_num)),
             ('x_so_number', '<=', int(to_so_num))])

        #         raise UserError(str(so_from_list.ids))
        #         lot_to_list = self.env['stock.production.lot'].search([('x_lot_name_char', '=', to_lot_char),('x_lot_name_number', '<=', int(to_lot_num))])

        from_sale_ids = self.env['sale.order'].search(
            [('state', 'not in', ('draft', 'cancel')), ('id', 'in', so_from_list.ids)])

        #         finish_mos = []
        #         for so_no in from_sale_ids:
        #             finish_mo_no = ''
        #             finish_mo_nos = self.env['mrp.production'].search([('origin','in', so_no.name), ('state','!=', 'cancel')])
        #             raise UserError(str(finish_mo_nos.name))
        #             for finish_mo in finish_mo_nos:
        #                 order_len = len(finish_mo.name)
        #                 if order_len > 11:
        #                     mo_no = finish_mo.name.split('-')
        # #                     raise UserError(str(mo_no))
        #                     finish_mo_no = mo_no[0]
        #                 else:
        #                     finish_mo_no = finish_mo.name
        #             finish_mos = set(finish_mo_no)
        #         raise UserError(str(finish_mos))
        owner_sale_ids = self.env['sale.order'].search(
            [('partner_id', 'in', docs.owner_ids.ids), ('state', 'not in', ('draft', 'cancel'))])

        so_owner_sale_ids = self.env['sale.order'].search(
            [('partner_id', 'in', docs.owner_ids.ids), ('id', 'in', so_from_list.ids),
             ('state', 'not in', ('draft', 'cancel'))])
        #         raise UserError(str(owner_sale_ids.ids))

        # owner_from_stock_ids = self.env['stock.move.line'].search(
        #     [('owner_id', 'in', owner_ids), ('location_id', '=', 9), ('location_dest_id', '=', 20),
        #      ('state', '=', 'done'), ('lot_id', 'in', lot_from_list.ids)])

        # owner_stock_ids = self.env['stock.move.line'].search(
        #     [('owner_id', 'in', owner_ids), ('location_id', '=', 9), ('location_dest_id', '=', 20),
        #      ('state', '=', 'done')])
        #         raise UserError(str(from_stock_ids.ids))
        #         to_stock_ids = self.env['stock.move.line'].search([('location_id.id','=', 9), ('location_dest_id.id','=', 20), ('state','=', 'done'), ('lot_id','in', lot_to_list.ids)])

        return {
            'docs': docs,
            'from_sale_ids': from_sale_ids,
            'owner_sale_ids': owner_sale_ids,
            'so_owner_sale_ids': so_owner_sale_ids,
            #             'to_stock_ids': to_stock_ids,
            'owner_ids': owner_ids,
            #             'stock_ids': stock_ids,
        }