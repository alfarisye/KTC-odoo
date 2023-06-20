
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class StockLandedCost(models.Model):
    _inherit = 'stock.landed.cost'

    datetime = fields.Datetime('Date', default=fields.Datetime.now(
    ), copy=False, required=True, states={'done': [('readonly', True)]}, tracking=True)


class StockLandedCostLine(models.Model):
    _inherit = 'stock.landed.cost.lines'

    location_id = fields.Many2one(
        'stock.location', string='Destination Location')
    percentage = fields.Float('Percentage')
