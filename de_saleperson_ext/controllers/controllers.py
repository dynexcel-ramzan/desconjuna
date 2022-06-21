# -*- coding: utf-8 -*-
# from odoo import http


# class DeSalepersonExt(http.Controller):
#     @http.route('/de_saleperson_ext/de_saleperson_ext/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_saleperson_ext/de_saleperson_ext/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_saleperson_ext.listing', {
#             'root': '/de_saleperson_ext/de_saleperson_ext',
#             'objects': http.request.env['de_saleperson_ext.de_saleperson_ext'].search([]),
#         })

#     @http.route('/de_saleperson_ext/de_saleperson_ext/objects/<model("de_saleperson_ext.de_saleperson_ext"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_saleperson_ext.object', {
#             'object': obj
#         })
