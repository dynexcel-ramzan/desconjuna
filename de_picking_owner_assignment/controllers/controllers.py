# -*- coding: utf-8 -*-
from odoo import http

# class DePickingOwnerMandatory(http.Controller):
#     @http.route('/de_picking_owner_mandatory/de_picking_owner_mandatory/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_picking_owner_mandatory/de_picking_owner_mandatory/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_picking_owner_mandatory.listing', {
#             'root': '/de_picking_owner_mandatory/de_picking_owner_mandatory',
#             'objects': http.request.env['de_picking_owner_mandatory.de_picking_owner_mandatory'].search([]),
#         })

#     @http.route('/de_picking_owner_mandatory/de_picking_owner_mandatory/objects/<model("de_picking_owner_mandatory.de_picking_owner_mandatory"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_picking_owner_mandatory.object', {
#             'object': obj
#         })