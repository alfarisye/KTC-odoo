
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    warehouse_id = fields.Many2one('stock.warehouse', 'Site')
    delivery_date = fields.Datetime('Delivery Date')
    request_by = fields.Char('Request by Mechanic')
    reason_delay = fields.Char('Reason Delay')
    substitute = fields.Boolean('Substitute')
    attachment = fields.Binary('Attachment')
    photos = fields.Binary('Photos')
    move_ids_substitute = fields.One2many(
        'stock.move', 'picking_id', string="Substitute Part", compute='_compute_move_ids_substitute')

    @api.depends('substitute', 'move_ids', 'move_ids.state')
    def _compute_move_ids_substitute(self):
        for picking in self:
            pass
