# -*- coding: utf-8 -*-
# from odoo import http


# class KtcEquipment(http.Controller):
#     @http.route('/ktc_equipment/ktc_equipment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ktc_equipment/ktc_equipment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ktc_equipment.listing', {
#             'root': '/ktc_equipment/ktc_equipment',
#             'objects': http.request.env['ktc_equipment.ktc_equipment'].search([]),
#         })

#     @http.route('/ktc_equipment/ktc_equipment/objects/<model("ktc_equipment.ktc_equipment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ktc_equipment.object', {
#             'object': obj
#         })
