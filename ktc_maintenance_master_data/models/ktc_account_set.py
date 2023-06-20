
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KtcAccountSet(models.Model):
    _description = 'Account Set'
    _name = 'ktc.md.account.set'

    name = fields.Char("Name", required=True)
    active = fields.Boolean("Active", default=True)

