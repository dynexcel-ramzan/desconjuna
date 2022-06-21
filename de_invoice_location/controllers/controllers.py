# -*- coding: utf-8 -*-
from odoo import http

# class DeInvoiceLocation(http.Controller):
#     @http.route('/de_invoice_location/de_invoice_location/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_invoice_location/de_invoice_location/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_invoice_location.listing', {
#             'root': '/de_invoice_location/de_invoice_location',
#             'objects': http.request.env['de_invoice_location.de_invoice_location'].search([]),
#         })

#     @http.route('/de_invoice_location/de_invoice_location/objects/<model("de_invoice_location.de_invoice_location"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_invoice_location.object', {
#             'object': obj
#         })