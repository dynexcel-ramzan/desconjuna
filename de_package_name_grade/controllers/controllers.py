# -*- coding: utf-8 -*-
from odoo import http

# class DeEquipmentMaintenanceName(http.Controller):
#     @http.route('/de_equipment_maintenance_name/de_equipment_maintenance_name/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_equipment_maintenance_name/de_equipment_maintenance_name/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_equipment_maintenance_name.listing', {
#             'root': '/de_equipment_maintenance_name/de_equipment_maintenance_name',
#             'objects': http.request.env['de_equipment_maintenance_name.de_equipment_maintenance_name'].search([]),
#         })

#     @http.route('/de_equipment_maintenance_name/de_equipment_maintenance_name/objects/<model("de_equipment_maintenance_name.de_equipment_maintenance_name"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_equipment_maintenance_name.object', {
#             'object': obj
#         })