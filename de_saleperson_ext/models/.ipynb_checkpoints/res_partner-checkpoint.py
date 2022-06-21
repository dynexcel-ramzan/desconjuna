from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    sale_person = fields.Many2one('hr.employee', string="Saleperson")
