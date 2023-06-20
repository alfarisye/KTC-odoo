
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

import datetime


class KtcMeterReading(models.Model):
    _name = 'ktc.meter.reading'
    _description = 'Meter/Measurement Reading'
    _rec_name = "equipment_id"

    equipment_id = fields.Many2one('ktc.equipment.master', string='Equipment')
    accumulative_hourmeter = fields.Float(string='Accumulative Hourmeter', 
        compute='_compute_accumulative_hourmeter' )
    accumulative_kilometer = fields.Float(string='Accumulative Kilometer', 
        compute='_compute_accumulative_kilometer' )
    meter_line_ids = fields.One2many('ktc.meter.reading.line', 'meter_reading_id', string='Meter Line')
    reset_line_ids = fields.One2many('ktc.reset.meter.line', 'meter_reading_id', string='Reset Line')

    @api.depends('meter_line_ids.start', 'meter_line_ids.end')
    def _compute_accumulative_hourmeter(self):
        for record in self:
            record_lines = record.meter_line_ids
            record.accumulative_hourmeter = sum(record_lines.mapped(lambda x: x["run_time"] if x.measuring_type == 'hourmeter' else 0))

    @api.depends('meter_line_ids.start', 'meter_line_ids.end')
    def _compute_accumulative_kilometer(self):
        for record in self:
            record_lines = record.meter_line_ids
            record.accumulative_kilometer = sum(record_lines.mapped(lambda x: x["run_time"] if x.measuring_type == 'kilometer' else 0))


class KtcMeterReadingLine(models.Model):
    _name = 'ktc.meter.reading.line'
    _description = 'KTcMEterREadingLIne'

    meter_reading_id = fields.Many2one('ktc.meter.reading', string='Meter Reading')
    measuring_date = fields.Date(string='Measuring Date')
    measuring_type = fields.Selection([
        ('hourmeter', 'Hourmeter'),
        ('kilometer', 'Kilometer')
    ], string='Measuring Type')
    start = fields.Integer('Start')
    end = fields.Integer('End')
    run_time = fields.Integer('Run Time', 
        compute='_compute_run_time' )
    
    @api.depends('start', 'end')
    def _compute_run_time(self):
        for record in self:
            record.run_time = record.end - record.start

    @api.onchange("measuring_date")
    def _onchange_date(self):
        the_date = self.measuring_date.strftime('%Y-%m-%d') if self.measuring_date else datetime.datetime.today().isoformat()
        meter_reading_id = self._origin.meter_reading_id.id if self.id else self.meter_reading_id._origin.id
        
        # get reset
        reset_record = self.env["ktc.reset.meter.line"].search([("reset_date", "<=", the_date), 
                                                                ("meter_reading_id", "=", meter_reading_id)], limit=1)
        # check if data already resetted
        last_record = self.env["ktc.meter.reading.line"].search([("meter_reading_id", "=", meter_reading_id)], limit=1, order="measuring_date DESC")

        result = 0
        if last_record and reset_record:
            result = 0 if last_record.start == reset_record.to_reading and last_record.measuring_date >= reset_record.reset_date else reset_record.to_reading

        self.start = result    

class KtcResetMeter(models.Model):
    _name = 'ktc.reset.meter.line'
    _description = 'Reset Meter'

    meter_reading_id = fields.Many2one('ktc.meter.reading', string='Meter Reading ID')
    reset_date = fields.Date('Reset Date')
    measuring_type = fields.Selection([
        ('hourmeter', 'Hourmeter'),
        ('kilometer', 'Kilometer')
    ], string='Measuring Type')
    from_reading = fields.Integer('From Reading')
    to_reading = fields.Integer('To Reading')

