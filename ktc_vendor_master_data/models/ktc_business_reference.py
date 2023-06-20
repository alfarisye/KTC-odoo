from odoo import _, api, fields, models
import logging

_logger = logging.getLogger(__name__)

class KTCBusinessReference(models.Model):
    _name = 'ktc.business.reference'
    _description = 'Business Reference'

    name = fields.Char(string='Business Reference')
    vendor_id = fields.Many2one('res.partner', string='Vendor')
    sequence = fields.Integer(string='Sequence')
    
    
    
