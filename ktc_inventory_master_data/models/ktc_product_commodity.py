
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class KtcProductCommodity(models.Model):
    _name = 'ktc.md.product.commodity'
    _description = 'Product Commodity'

    name = fields.Char("Name", required=True)
    active = fields.Boolean("Active", default=True)
    description = fields.Char('Description')
