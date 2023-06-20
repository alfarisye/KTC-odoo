# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ktc_equipment(models.Model):
#     _name = 'ktc_equipment.ktc_equipment'
#     _description = 'ktc_equipment.ktc_equipment'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
