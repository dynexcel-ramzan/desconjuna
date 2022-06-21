# -*- coding: utf-8 -*-
from odoo import http

# class DeAmountWords(http.Controller):
#     @http.route('/de_amount_words/de_amount_words/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_amount_words/de_amount_words/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_amount_words.listing', {
#             'root': '/de_amount_words/de_amount_words',
#             'objects': http.request.env['de_amount_words.de_amount_words'].search([]),
#         })

#     @http.route('/de_amount_words/de_amount_words/objects/<model("de_amount_words.de_amount_words"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_amount_words.object', {
#             'object': obj
#         })