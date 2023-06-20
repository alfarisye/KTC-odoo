
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

from datetime import date


class KtcEquipmentMaster(models.Model):
    _name = 'ktc.equipment.master'
    _description = 'Equipment Master List'

    name = fields.Char(string="Unit ID/Component ID")
    category_id = fields.Many2one('ktc.md.category', string='Category')
    brand_id = fields.Many2one('ktc.md.brand', string='Brand')
    model_id = fields.Many2one('ktc.md.model', string='Model')
    class_id = fields.Many2one('ktc.md.class', string='Class')
    site_id = fields.Many2one('ktc.md.site', string='Site')
    description = fields.Text("Description")
    machine_code_id = fields.Many2one('ktc.md.machine.code', string='Machine Code')
    machine_type_id = fields.Many2one('ktc.md.machine.type', string='Machine Type')
    machine_category_id = fields.Many2one('ktc.md.machine.category', string='Machine Category')
    width = fields.Float(string='Width')
    weight = fields.Float(string='Weight')
    length = fields.Float(string='Length')
    height = fields.Float(string='Height')
    serial_number = fields.Char(string='Serial Number')
    manufacturing_year = fields.Integer(string='Manufacturing Year')
    age = fields.Float(string='Age', 
        compute='_compute_equipment_age' )
    equipment_image = fields.Image('Equipment Image')
    measurement_id = fields.Many2one("ktc.meter.reading", string="Measurement ID", 
        compute='_get_measurement_id' )
    last_hourmeter = fields.Float("Hourmeter", 
        compute='_compute_last_measurement' )
    last_kilometer = fields.Float("Kilometer", 
        compute='_compute_last_measurement' )
    accumulative_hourmeter = fields.Float(string='Accumulative Hourmeter', 
        related='measurement_id.accumulative_hourmeter' )
    accumulative_kilometer = fields.Float(string='Accumulative Kilometer', 
        related='measurement_id.accumulative_kilometer' )
    warrant_type_id = fields.Many2one('ktc.md.warranty.type', string='Warranty Type')
    warrant_start_date = fields.Date('Warranty Start Date')
    warrant_end_date = fields.Date('Warranty End Date')
    warrant_hourmeter = fields.Float('Warrant Hourmeter')
    warrant_kilometer = fields.Float('Warrant Kilometer')

    """
    TODO: 
        1. Tab maintenance history.
        2. Transfer information. 
    """

    @api.depends('measurement_id')
    def _compute_last_measurement(self):
        for record in self:
            last_hourmeter_line = self.env['ktc.meter.reading.line'].search([('meter_reading_id', '=', record.measurement_id.id), ('measuring_type', '=', 'hourmeter')], order="measuring_date DESC", limit=1)
            last_odoometer_line = self.env['ktc.meter.reading.line'].search([('meter_reading_id', '=', record.measurement_id.id), ('measuring_type', '=', 'kilometer')], order="measuring_date DESC", limit=1)
            record.last_hourmeter = last_hourmeter_line.run_time
            record.last_kilometer = last_odoometer_line.run_time
    
    def _get_measurement_id(self):
        for record in self:
            rec_measurement = self.env['ktc.meter.reading'].search([("equipment_id", "=", record.id)], limit=1, order="id")
            record.measurement_id = rec_measurement.id
    
    @api.depends('manufacturing_year')
    def _compute_equipment_age(self):
        for record in self:
            today = date.today()
            age = today.year - record.manufacturing_year
            record.age = age
    
    

    
    
    

    

    
    

