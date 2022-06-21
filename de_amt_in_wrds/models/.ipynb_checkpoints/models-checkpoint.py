# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools, _

try:
    from num2words import num2words
except ImportError:
    _logger.warning("The num2words python library is not installed, amount-to-text features won't be fully available.")
    num2words = None

# -*- coding: utf-8 -*-

from copy import deepcopy
import logging
import math
import time
from datetime import date
from collections import OrderedDict, defaultdict
from odoo import api, fields, models, _
from odoo.osv import expression
from odoo.exceptions import RedirectWarning, UserError, ValidationError
from odoo.tools.misc import formatLang, format_date
from odoo.tools import float_is_zero, float_compare
from odoo.tools.safe_eval import safe_eval
from odoo.addons import decimal_precision as dp
from lxml import etree


_logger = logging.getLogger(__name__)

#----------------------------------------------------------
# Entries
#----------------------------------------------------------

class AccountInvoice(models.Model):
    _inherit= "account.invoice"
    
    amt_word = fields.Char(string='Amount Word', compute='_compute_amt_in_word', store=True)
    decimal_places = fields.Integer(compute='_compute_decimal_places', store=True)
    rounding = fields.Float(string='Rounding Factor', digits=(12, 6), default=0.01)
#     currency_unit_label = fields.Char(string="Currency Unit", help="Currency Unit Name")
#     currency_subunit_label = fields.Char(string="Currency Subunit", help="Currency Subunit Name")
    
    def _compute_amt_in_word(self):
        for rec in self:
            rec.amt_word = rec.amount_to_text(rec.amount_total) + ' Only'
    
    @api.multi
    @api.depends('rounding')
    def _compute_decimal_places(self):
        for currency in self:
            if 0 < currency.rounding < 1:
                currency.decimal_places = int(math.ceil(math.log10(1/currency.rounding)))
            else:
                currency.decimal_places = 0
    
    @api.multi
    def amount_to_text(self, amount):
        self.ensure_one()
        def _num2words(number, lang):
            try:
                return num2words(number, lang=lang).title()
            except NotImplementedError:
                return num2words(number, lang='en').title()

        if num2words is None:
            logging.getLogger(__name__).warning("The library 'num2words' is missing, cannot render textual amounts.")
            return ""

        formatted = "%.{0}f".format(self.decimal_places) % amount
        parts = formatted.partition('.')
        integer_value = int(parts[0])
        fractional_value = int(parts[2] or 0)

        lang_code = self.env.context.get('lang') or self.env.user.lang
        lang = self.env['res.lang'].with_context(active_test=False).search([('code', '=', lang_code)])
        amount_words = tools.ustr('{amt_value} {amt_word}').format(
                        amt_value=_num2words(integer_value, lang=lang.iso_code),
                        amt_word=self.currency_id.currency_unit_label,
                        )
        if not self.is_zero(amount - integer_value):
            amount_words += ' ' + _('and') + tools.ustr(' {amt_value} {amt_word}').format(
                        amt_value=_num2words(fractional_value, lang=lang.iso_code),
                        amt_word=self.currency_id.currency_subunit_label,
                        )
        return amount_words
    
    @api.multi
    def is_zero(self, amount):
        """Returns true if ``amount`` is small enough to be treated as
           zero according to current currency's rounding rules.
           Warning: ``is_zero(amount1-amount2)`` is not always equivalent to
           ``compare_amounts(amount1,amount2) == 0``, as the former will round after
           computing the difference, while the latter will round before, giving
           different results for e.g. 0.006 and 0.002 at 2 digits precision.

           :param float amount: amount to compare with currency's zero

           With the new API, call it like: ``currency.is_zero(amount)``.
        """
        return tools.float_is_zero(amount, precision_rounding=self.rounding)