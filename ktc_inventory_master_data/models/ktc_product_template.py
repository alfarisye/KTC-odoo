
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_STATUS = [
    ("active", "Active"),
    ("non_active", "Non Active"),
]


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    description = fields.Char('Description')
    stock_code = fields.Integer('Stockode')
    brand_id = fields.Many2one('ktc.md.brand', string='Brand')
    size = fields.Char('Size')
    product_class_id = fields.Many2one(
        'ktc.md.product.class', string='Product Class')
    product_commodity_id = fields.Many2one(
        'ktc.md.product.commodity', string='Product Commodity')
    product_category_id = fields.Many2one(
        'ktc.md.product.category', string='Product Categories')
    ktc_category_id = fields.Many2one(
        'ktc.md.inventory.category', string='KTC Category')
    shelf_life = fields.Char('Shelf Life')
    physical_number = fields.Integer('Physical Number')
    status = fields.Selection(
        selection=_STATUS, string='Status')
    obsolete = fields.Boolean('Obsolete')
    new_part_number = fields.Integer('New Part Number')
    original_part_number = fields.Char('Original Part Number')
    manufacturer_part_number = fields.Char('Manufacturer Part Number')
    warehouse_id = fields.Many2one('stock.warehouse', string='Warehouse')
    shelf_location = fields.Char('Shelf Location')
    bin_location = fields.Char('Bin Location')
    reflenishment_status = fields.Char('Reflenishment Status')
    reason = fields.Char('Reason')
    attachment = fields.Binary('Upload Photos')
