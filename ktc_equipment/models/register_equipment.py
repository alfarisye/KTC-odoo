
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError



class RegisterEquipment(models.Model):
    _name = 'ktc.register.equipment'
    _description = 'Request Register Equipment'

    name = fields.Char("Request Register Unit")
    equipment_image = fields.Image('Equipment Image')
    category_id = fields.Many2one('ktc.md.category', string='Category')
    brand_id = fields.Many2one(comodel_name='ktc.md.brand', string='Brand')
    model_id = fields.Many2one(comodel_name='ktc.md.model', string='Model')
    class_id = fields.Many2one('ktc.md.class', string='Class')
    site_id = fields.Many2one('ktc.md.site', string='Site')
    description = fields.Char('Description')
    machine_code_id = fields.Many2one('ktc.md.machine.code', string='Machine Code')
    machine_category_id = fields.Many2one('ktc.md.machine.category', string='Machine Category')
    machine_type_id = fields.Many2one('ktc.md.machine.type', string='Machine Type')
    width = fields.Float('Width')
    weight = fields.Float('Weight')
    length = fields.Float('Length')
    height = fields.Float('Height')
    serial_number = fields.Char('Serial Number')
    manufacturing_year = fields.Integer('Manufacturing Year')
    warrant_type_id = fields.Many2one('ktc.md.warranty.type', string='Warranty Type')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    hourmeter = fields.Float('Hourmeter')
    kilometer = fields.Float('Kilometer')
    state = fields.Selection([
            ('draft', 'Draft'),
            ('in_progress', 'In Progress'),
            ('done', 'Done'),
        ], string='Status', default='draft', required=True
    )

    def to_progress(self):
        return self.write({"state": "in_progress"})

    def to_done(self):
        """
        TODO: 
        1. copy data warranty ke ktc.equipment.master
        """
        source_data = {
            'name': self.name,
            'equipment_image': self.equipment_image,
            'category_id': self.category_id.id,
            'brand_id': self.brand_id.id,
            'model_id': self.model_id.id,
            'class_id': self.class_id.id,
            'site_id': self.site_id.id,
            'description': self.description,
            'machine_code_id': self.machine_code_id.id,
            'machine_category_id': self.machine_category_id.id,
            'machine_type_id': self.machine_type_id.id,
            'width': self.width,
            'weight': self.weight,
            'length': self.length,
            'height': self.height,
            'serial_number': self.serial_number,
            'manufacturing_year': self.manufacturing_year,
            'warrant_type_id': self.warrant_type_id.id,
            'warrant_start_date': self.start_date,
            'warrant_end_date': self.end_date,
            'warrant_hourmeter': self.hourmeter,
            'warrant_kilometer': self.kilometer,
        }
        res = self.env["ktc.equipment.master"].create(source_data)
        self.write({"state": "done"})
        return res

    
    

