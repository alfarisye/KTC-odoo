
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KtcSiteMd(models.Model):
    _description = 'Site Master Data'
    _name = 'ktc.md.site'

    name = fields.Char("Name", required=True)
    active = fields.Boolean("Active", default=True)
    
