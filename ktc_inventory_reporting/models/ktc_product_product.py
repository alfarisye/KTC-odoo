
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class ProductProduct(models.Model):
    _inherit = 'product.product'

    status = fields.Char('Status')
    discrepancy = fields.Integer('Discrepancy')
    blind_cost = fields.Boolean('Blind Cost')
    approval = fields.Selection([
        ('approve', 'approve'),
        ('reject', 'reject'),
    ], string='Approval')
    date = fields.Datetime(
        'Date', default=fields.Datetime.now())
    attachment = fields.Binary('Attachment')
