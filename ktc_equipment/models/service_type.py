
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KtcServiceType(models.Model):
    _name = 'ktc.service.type'
    _description = 'Service Type'

    name = fields.Char('Service Type', required=True)
    schedule_maintenance_group_id = fields.Many2one('ktc.md.schedule.maintenance', string='Schedule Maintenance Group')
    description = fields.Char('Description')
    service_internal = fields.Integer(
        string='Service Internal',
    )
    service_package_id = fields.Many2one('ktc.service.package', string='Service Package')
    task_list_id = fields.Many2one(
        string='Task List',
        comodel_name='ktc.standard.tasklist',
        ondelete='restrict',
    )
    
    
    

    
