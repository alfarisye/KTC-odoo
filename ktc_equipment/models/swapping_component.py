
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KtcSwappingComponent(models.Model):
    _name = 'ktc.swapping.component'
    _description = 'Swapping Component'

    name = fields.Char(string='Swap Transaction Number')
    component_id = fields.Many2one('ktc.equipment.master', string='Component ID')
    serial_number = fields.Char(string='Serial Number')
    part_number = fields.Char(string='Part Number')

    old_parent = fields.Many2one('ktc.equipment.master', string='Old Parent')
    old_uninstall_date = fields.Date(string='Uninstall Date')
    old_uninstall_hm = fields.Float(string='Uninstall HM')
    old_uninstall_km = fields.Float(string='Uninstall KM')
    work_order = fields.Char(string='Work Order')

    new_parent = fields.Many2one('ktc.equipment.master', string='New Parent')
    new_install_date = fields.Date(string='Installation Date')
    new_install_hm = fields.Float(string='Installation HM')
    new_install_km = fields.Float(string='Installation KM')
    
    
    
    
    