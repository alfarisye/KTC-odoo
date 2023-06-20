
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_STATE = [
    ("draft", "Draft"),
    ("done", "Done"),
]


class KtcSalvagedMaterial(models.Model):
    _name = 'ktc.salvaged.material'
    _description = 'Salvaged Material Deposit'

    name = fields.Char("Name", required=True)
    active = fields.Boolean("Active", default=True)
    state = fields.Selection(selection=_STATE, string='State', default='draft')
    request_by = fields.Char('Request by Mechanic')
    warehouse_id = fields.Many2one('stock.warehouse', string='Site')
    maintenance_request_id = fields.Many2one(
        'maintenance.request', string='Work Order')
    gr_number_id = fields.Many2one('stock.picking', string='GR Number')
    gi_number_id = fields.Many2one('stock.picking', string='GI Number')
    date = fields.Datetime('Deposit Date', default=fields.Datetime.now())
    description = fields.Char('Description')
    attachment = fields.Binary('Attachment')
    salvaged_material_ids = fields.One2many(
        'ktc.salvaged.material.line', 'salvaged_material_id', string='Salvaged Material Lines')

    def action_request_md_material(self):
        for rec in self:
            pass


class KtcSalvagedMaterialLine(models.Model):
    _name = 'ktc.salvaged.material.line'
    _description = 'Salvaged Material Deposit Line'

    salvaged_material_id = fields.Many2one(
        'ktc.salvaged.material', string='Salvaged Material ID')
    currency_id = fields.Many2one('res.currency', string='Currency')
    product_id = fields.Many2one('product.product', string='Product')
    manufacturer_part_number = fields.Char(
        'Manufacturer Part Number', related='product_id.manufacturer_part_number')
    artificial_cost = fields.Monetary('Artificial Cost')
    quantity = fields.Integer('Quantity')
    product_uom = fields.Many2one('uom.uom', string='Unit of Measure')
