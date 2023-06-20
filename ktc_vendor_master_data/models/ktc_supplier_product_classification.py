from odoo import _, api, fields, models
import logging

_logger = logging.getLogger(__name__)

class KTCSupplierProductClassification(models.Model):
    _name = 'ktc.supplier.product.classification'
    _description = 'Supplier Product Classification'

    name = fields.Char(string='Supplier Product Classification')
    active = fields.Boolean(string='Active', default=True)