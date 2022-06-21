# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AnalyticTags(models.Model):
    _inherit = 'account.analytic.tag'

    sequence = fields.Char(string="Sequence", store=True)
