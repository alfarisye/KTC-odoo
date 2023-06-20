
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError



class StandardTasklist(models.Model):
    _name = 'ktc.standard.tasklist'
    _description = 'Standard Tasklist'

    name = fields.Char("Task Name")
    schedule_maintenance_group_id = fields.Many2one('ktc.md.schedule.maintenance', string='Schedule Maintenance Group')
    service_type_id = fields.Many2one(
        string='Service Type',
        comodel_name='ktc.service.type',
        ondelete='restrict',
    )
    tasklist_line_ids = fields.One2many('ktc.standard.tasklist.line', 'task_id', string='Tasklist Line')


class StandardTasklistLine(models.Model):
    _name = 'ktc.standard.tasklist.line'
    _description = 'Standard Tasklist Line'

    _rec_name = 'name'
    _order = 'name ASC'

    task_id = fields.Many2one('ktc.standard.tasklist', string='Task ID')
    name = fields.Char(
        string='Task Code',
        required=True,
        default=lambda self: _('New'),
        copy=False
    )
    desc = fields.Char('Description')
    skill_set = fields.Selection([
        ('test', 'test 123')
    ], string='Skill Set')

