# -*- coding: utf-8 -*-
# from odoo import http


# class HitMaintenanceMasterData(http.Controller):
#     @http.route('/hit_maintenance_master_data/hit_maintenance_master_data', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hit_maintenance_master_data/hit_maintenance_master_data/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hit_maintenance_master_data.listing', {
#             'root': '/hit_maintenance_master_data/hit_maintenance_master_data',
#             'objects': http.request.env['hit_maintenance_master_data.hit_maintenance_master_data'].search([]),
#         })

#     @http.route('/hit_maintenance_master_data/hit_maintenance_master_data/objects/<model("hit_maintenance_master_data.hit_maintenance_master_data"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hit_maintenance_master_data.object', {
#             'object': obj
#         })
