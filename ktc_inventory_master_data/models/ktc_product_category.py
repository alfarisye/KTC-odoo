
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class KtcProductCategory(models.Model):
    _name = 'ktc.md.product.category'
    _description = 'Product Category'

    name = fields.Char("Product Category", required=True)
    active = fields.Boolean("Active", default=True)
