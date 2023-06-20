
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KtcServicePackage(models.Model):
    _name = 'ktc.service.package'
    _description = 'Service Package'

    name = fields.Char('Application Part List', required=True)
    schedule_maintenance_group_id = fields.Many2one('ktc.md.schedule.maintenance', string='Schedule Maintenance Group')
    description = fields.Char('Description')
    service_package_item_ids = fields.One2many('ktc.service.package.item', 'service_package_id', string='Service Package Item')
    service_package_warranty_ids = fields.One2many('ktc.service.package.warranty', 'service_package_id', string='Service Package Warranty')


class KtcServicePackageItem(models.Model):
    _name = 'ktc.service.package.item'
    _description = "Service Package Item"

    _rec_name = "service_package_id"

    service_package_id = fields.Many2one('ktc.service.package', string='Service Package')
    product_id = fields.Many2one(
        string='Product',
        comodel_name='product.template',
        ondelete='restrict',
    )
    internal_reference = fields.Char(string='Internal Reference', related='product_id.default_code')
    qty = fields.Integer(string='Qty')
    uom_id = fields.Many2one(
        string='UoM',
        comodel_name='uom.uom',
        related='product_id.uom_id'
    )
    manufacturer_part_number = fields.Char('Manufacturer Part Number', related='product_id.manufacturer_part_number')
    remark = fields.Char(string='Remark')    


class KtcServicePackageWarranty(models.Model):
    _name = 'ktc.service.package.warranty'
    _description = "Service Package Warranty"

    _rec_name = "service_package_id"

    service_package_id = fields.Many2one('ktc.service.package', string='Service Package')
    product_id = fields.Many2one(
        string='Product',
        comodel_name='product.template',
        ondelete='restrict',
    )
    qty = fields.Integer(string='Qty')
    internal_reference = fields.Char(string='Internal Reference', related='product_id.default_code')
    uom_id = fields.Many2one(
        string='UoM',
        comodel_name='uom.uom',
        related='product_id.uom_id'
    )
    manufacturer_part_number = fields.Char('Manufacturer Part Number', related='product_id.manufacturer_part_number')
    remark = fields.Char(string='Remark')
    
    
    

    
