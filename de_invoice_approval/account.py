from odoo import api, fields, models, _
from odoo.exceptions import RedirectWarning, UserError, ValidationError, AccessError
from odoo.tools import float_compare, date_utils, email_split, email_re
from odoo.tools.misc import formatLang, format_date, get_lang

from datetime import date, timedelta
from collections import defaultdict
from itertools import zip_longest
from hashlib import sha256
from json import dumps

import ast
import json
import re
import warnings


class account_move(models.Model):
    _inherit = 'account.move'

    is_approval = fields.Boolean(string="Is Approval", store=True)

    def action_approval(self):
        self._post(soft=False)
        self.write({'state': 'approval', 'is_approval': True})

    def action_post(self):
        if self.is_approval == True:
            self.write({'state': 'posted'})
            return False
        else:
            self._post(soft=False)
            return False
        # self._post(soft=False)
