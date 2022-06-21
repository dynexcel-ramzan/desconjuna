import json
import datetime
import math
import operator as py_operator
import re

from collections import defaultdict
from dateutil.relativedelta import relativedelta
from itertools import groupby

from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError
from odoo.tools import float_compare, float_round, float_is_zero, format_datetime
from odoo.tools.misc import format_date

from odoo.addons.stock.models.stock_move import PROCUREMENT_PRIORITIES

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def _post_inventory(self, cancel_backorder=False):
        for order in self:
            moves_not_to_do = order.move_raw_ids.filtered(lambda x: x.state == 'done')
            moves_to_do = order.move_raw_ids.filtered(lambda x: x.state not in ('done', 'cancel'))
            for move in moves_to_do.filtered(lambda m: m.product_qty == 0.0 and m.quantity_done > 0):
                move.product_uom_qty = move.quantity_done
            # MRP do not merge move, catch the result of _action_done in order
            # to get extra moves.
            moves_to_do = moves_to_do._action_done()
            moves_to_do = order.move_raw_ids.filtered(lambda x: x.state == 'done') - moves_not_to_do

            finish_moves = order.move_finished_ids.filtered(lambda m: m.product_id == order.product_id and m.state not in ('done', 'cancel'))
            # the finish move can already be completed by the workorder.
            if not finish_moves.quantity_done:
                finish_moves.quantity_done = float_round(order.qty_producing - order.qty_produced, precision_rounding=order.product_uom_id.rounding, rounding_method='HALF-UP')
                finish_moves.move_line_ids.lot_id = order.lot_producing_id
            order._cal_price(moves_to_do)

            moves_to_finish = order.move_finished_ids.filtered(lambda x: x.state not in ('done', 'cancel'))
            moves_to_finish = moves_to_finish._action_done()
            order.action_assign()
            consume_move_lines = moves_to_do.mapped('move_line_ids')
            order.move_finished_ids.move_line_ids.consume_line_ids = [(6, 0, consume_move_lines.ids)]
        return True
