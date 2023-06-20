
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KtcTireForm(models.Model):
    _name = 'ktc.tire.form'
    _description = 'Tire E Form'

    name = fields.Char('Tire Transaction', required=True)
    tire_sn = fields.Selection(string='Tire S/N', selection=[('option_1', 'Option 1'), ('option_2', 'Option 2'),])
    brand = fields.Char(string='Brand')
    size = fields.Char(string='Size')
    thread_new = fields.Float(string='Thread New (mm)')
    equipment_master_id = fields.Many2one('ktc.equipment.master', string='Unit ID')
    site_id = fields.Many2one('ktc.md.site', string='site')
    position = fields.Char(string='Position')
    tire_installation_date = fields.Date(string='Tire Installation Date')
    hm_installation_date = fields.Date(string='HM Installation Date')
    km_installation_date = fields.Date(string='KM Installation Date')
    hm_installation = fields.Float(string='HM Installation')
    km_installation = fields.Float(string='KM Installation')
    tire_replacement_date = fields.Date(string='Tire Replacement Date')
    hm_damage = fields.Float(string='HM Damage')
    km_damage = fields.Float(string='KM Damage')
    tread_condition = fields.Float(string='Tread Condition (mm)')
    tire_status = fields.Selection([
        ('state_1', 'State 1')
    ], string='Status')
    tire_action = fields.Selection([
        ('action_1', 'Action 1')
    ], string='Action')
    total_day = fields.Float(string='Total Day')
    lifetime_hm = fields.Float(string='Lifetime HM')
    lifetime_km = fields.Float(string='Lifetime KM')
    accumulative_hm = fields.Float(string='Accumulative Lifetime HM')
    accumulative_km = fields.Float(string='Accumulative Lifetime KM')
    accumulative_total_day = fields.Float(string='Accumulative Accumulative Total Day')
    file_upload = fields.Binary(string='Attachment')
    file_name = fields.Char('File Name')
    

    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    

    
