
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_RANGE_PRICE = [
    ("A", "Up to Rp6,000,000"),
    ("B", "Rp600,000 - Rp5,999,999"),
    ("C", "Rp0 - Rp599,999"),
]


class KtcInventoryCategory(models.Model):
    _name = 'ktc.md.inventory.category'
    _description = 'KTC Category'

    name = fields.Char("Code", required=True)
    active = fields.Boolean("Active", default=True)
    range_price = fields.Selection(
        selection=_RANGE_PRICE, string='Range Price')
