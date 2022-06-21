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
    _name = 'report.de_greige_stock_status_report.greige_stock_report_pdf'
    _description = 'Greige Stock Status information'

    def _get_report_values(self, docids, data=None):
        model = self.env.context.get('active_model')
        docs = self.env['greige.stock.report.wizard'].browse(self.env.context.get('active_id'))
        from_lot_id = docs.from_lot_id.name
        to_lot_id = docs.to_lot_id.name
        owner_ids = docs.owner_ids.ids
        owner_from_stock_ids = ''
        from_stock_ids = ''
        to_stock_ids = ''
        from_lot_char = ''
        to_lot_char = ''
        from_lot_num = ''
        to_lot_num = ''
        #       Get From Lot Charachter
        if from_lot_id:
            for from_char in from_lot_id:
                from_lot_char = from_char
                break
            #       End From Lot Charachter
            #       Get From Lot Num
            from_count = 0
            for nchar in from_lot_id:
                from_count += 1
                if from_count > 1:
                    from_lot_num += nchar
        #       Get TO Lot Char
        if to_lot_id:
            for to_nchar in to_lot_id:
                to_lot_char = to_nchar
                break
            #       End To Lot Charachter

            #       Get To Lot NUmber
            to_count = 0
            for to_nchar in to_lot_id:
                to_count += 1
                if to_count > 1:
                    to_lot_num += to_nchar

        from_lot_num = int(from_lot_num) if from_lot_num != '' else 0
        to_lot_num = int(to_lot_num) if to_lot_num != '' else 0
        #         raise UserError(str(to_lot_num))
        #       End To Lot Number
        lot_from_list = self.env['stock.production.lot'].search(
            [('x_lot_name_char', '=', from_lot_char), ('x_lot_name_number', '>=', int(from_lot_num)),
             ('x_lot_name_number', '<=', int(to_lot_num))])

        #         raise UserError(str(lot_from_list.ids))
        #         lot_to_list = self.env['stock.production.lot'].search([('x_lot_name_char', '=', to_lot_char),('x_lot_name_number', '<=', int(to_lot_num))])

        from_stock_ids = self.env['stock.move.line'].search(
            [('location_id', '=', 9), ('location_dest_id', '=', 20), ('state', '=', 'done'),
             ('lot_id', 'in', lot_from_list.ids)])

        owner_from_stock_ids = self.env['stock.move.line'].search(
            [('owner_id', 'in', owner_ids), ('location_id', '=', 9), ('location_dest_id', '=', 20),
             ('state', '=', 'done'), ('lot_id', 'in', lot_from_list.ids)])

        owner_stock_ids = self.env['stock.move.line'].search(
            [('owner_id', 'in', owner_ids), ('location_id', '=', 9), ('location_dest_id', '=', 20),
             ('state', '=', 'done')])
        #         raise UserError(str(from_stock_ids.ids))
        #         to_stock_ids = self.env['stock.move.line'].search([('location_id.id','=', 9), ('location_dest_id.id','=', 20), ('state','=', 'done'), ('lot_id','in', lot_to_list.ids)])

        return {
            'docs': docs,
            'from_stock_ids': from_stock_ids,
            'owner_from_stock_ids': owner_from_stock_ids,
            'owner_stock_ids': owner_stock_ids,
            #             'to_stock_ids': to_stock_ids,
            'owner_ids': owner_ids,
            #             'stock_ids': stock_ids,
        }