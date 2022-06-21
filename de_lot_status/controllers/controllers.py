# -*- coding: utf-8 -*-
from odoo import http

# class DeLotStatus(http.Controller):
#     @http.route('/de_lot_status/de_lot_status/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_lot_status/de_lot_status/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_lot_status.listing', {
#             'root': '/de_lot_status/de_lot_status',
#             'objects': http.request.env['de_lot_status.de_lot_status'].search([]),
#         })

#     @http.route('/de_lot_status/de_lot_status/objects/<model("de_lot_status.de_lot_status"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_lot_status.object', {
#             'object': obj
#         })