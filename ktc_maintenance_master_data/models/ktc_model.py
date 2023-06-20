
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KtcModel(models.Model):
    _description = 'Model'
    _name = 'ktc.md.model'

    name = fields.Char("Name", required=True)
    active = fields.Boolean("Active", default=True)
    attachment = fields.Binary('Attachment')
    file_name = fields.Char('File Name')

