# -*- coding: utf-8 -*-
from odoo import http

# class DeInvoicePackage(http.Controller):
#     @http.route('/de_invoice_package/de_invoice_package/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_invoice_package/de_invoice_package/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_invoice_package.listing', {
#             'root': '/de_invoice_package/de_invoice_package',
#             'objects': http.request.env['de_invoice_package.de_invoice_package'].search([]),
#         })

#     @http.route('/de_invoice_package/de_invoice_package/objects/<model("de_invoice_package.de_invoice_package"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_invoice_package.object', {
#             'object': obj
#         })