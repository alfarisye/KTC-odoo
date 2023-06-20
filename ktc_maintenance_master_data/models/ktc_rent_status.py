
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KtcRentStatus(models.Model):
    _description = 'Rent Status Master Data'
    _name = 'ktc.md.rent.status'

    name = fields.Char("Name", required=True)
    active = fields.Boolean("Active", default=True)
    
