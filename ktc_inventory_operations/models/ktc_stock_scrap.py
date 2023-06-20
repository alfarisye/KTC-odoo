
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date, timedelta


class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    date = fields.Datetime(
        'Creation Date', default=fields.Datetime.now())
    attachment = fields.Binary('Attach File')
