
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class KtcProductClass(models.Model):
    _name = 'ktc.md.product.class'
    _description = 'Product Class'

    name = fields.Char("Class", required=True)
    active = fields.Boolean("Active", default=True)
