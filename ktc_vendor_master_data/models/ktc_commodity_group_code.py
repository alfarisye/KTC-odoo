from odoo import _, api, fields, models
import logging

_logger = logging.getLogger(__name__)

class KTCCommodityGroupCode(models.Model):
    _name = 'ktc.commodity.group.code'
    _description = 'Commodity Group Code'

    name = fields.Char(string='Commodity Group Code')
    active = fields.Boolean(string='Active', default=True)
    
    
