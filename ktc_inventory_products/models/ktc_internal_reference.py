
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

_STATUS = [
    ("active", "Active"),
    ("non_active", "Non Active"),
]


class KtcInternalReference(models.Model):
    _name = 'ktc.internal.reference'
    _description = 'Internal Reference'

    name = fields.Char("Name", required=True)
    active = fields.Boolean("Active", default=True)
    state = fields.Selection(selection=_STATE, string='State', default='draft')
    account_set_id = fields.Many2one(
        'ktc.md.account.set', string='Account Set')
    account_set_description = fields.Char(
        "Account Set Description", related='account_set_id.description')
    product_commodity_id = fields.Many2one(
        'ktc.md.product.commodity', string='Product Commodity')
    product_commodity_description = fields.Char(
        "Product Commodity Description", related='product_commodity_id.description')
    primary_product_ids = fields.One2many(
        'ktc.internal.reference.primary.line', 'internal_reference_id', string='Primary Product')
    substitute_product_ids = fields.One2many(
        'ktc.internal.reference.substitute.line', 'internal_reference_id', string='Substitute Product')


class KtcInternalReferencePrimaryLine(models.Model):
    _name = 'ktc.internal.reference.primary.line'
    _description = 'Internal Reference Primary Line'

    internal_reference_id = fields.Many2one(
        'ktc.internal.reference', string='Internal Reference ID')
    product_id = fields.Many2one('product.product', string='Product')
    manufacturer_part_number = fields.Char(
        'Manufacturer Part Number', related='product_id.manufacturer_part_number')
    product_class_id = fields.Many2one(
        'ktc.md.product.class', string='Product Class', related='product_id.product_class_id')
    brand_id = fields.Many2one(
        'ktc.md.brand', string='Brand', related='product_id.brand_id')
    status = fields.Selection(selection=_STATUS, string='Status')


class KtcInternalReferenceSubstituteLine(models.Model):
    _name = 'ktc.internal.reference.substitute.line'
    _description = 'Internal Reference Substitute Line'

    internal_reference_id = fields.Many2one(
        'ktc.internal.reference', string='Internal Reference ID')
    product_id = fields.Many2one('product.product', string='Product')
    manufacturer_part_number = fields.Char(
        'Manufacturer Part Number', related='product_id.manufacturer_part_number')
    product_class_id = fields.Many2one(
        'ktc.md.product.class', string='Product Class', related='product_id.product_class_id')
    brand_id = fields.Many2one(
        'ktc.md.brand', string='Brand', related='product_id.brand_id')
    status = fields.Selection(selection=_STATUS, string='Status')
