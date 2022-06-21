# -*- coding: utf-8 -*-
# from odoo import http


# class DeStockClothDesc(http.Controller):
#     @http.route('/de_stock_cloth_desc/de_stock_cloth_desc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_stock_cloth_desc/de_stock_cloth_desc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_stock_cloth_desc.listing', {
#             'root': '/de_stock_cloth_desc/de_stock_cloth_desc',
#             'objects': http.request.env['de_stock_cloth_desc.de_stock_cloth_desc'].search([]),
#         })

#     @http.route('/de_stock_cloth_desc/de_stock_cloth_desc/objects/<model("de_stock_cloth_desc.de_stock_cloth_desc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_stock_cloth_desc.object', {
#             'object': obj
#         })
