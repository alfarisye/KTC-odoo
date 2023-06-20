
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class StockMove(models.Model):
    _inherit = "stock.move"

    categ_id = fields.Many2one(
        'ktc.internal.reference', string='Internal Reference')
    manufacturer_part_number = fields.Char(
        'Manufacturer Part Number', related='product_id.manufacturer_part_number')
    quantity_done = fields.Integer('Done')
    quantity_reserved = fields.Integer('Reserved')
    quantity_delivery = fields.Integer('Delivery Qty')
    quantity_actual_receipt = fields.Integer('Actual Receipt')
    transfer_priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priorities")
    attachment = fields.Binary('Attachment')
    substitute = fields.Boolean('Substitute')
