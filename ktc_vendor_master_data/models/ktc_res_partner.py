from odoo import _, api, fields, models
import logging

_logger = logging.getLogger(__name__)

class KTCResPartnerInheritMasterData(models.Model):
    _inherit = 'res.partner'

    holding_company = fields.Char(string='Holding Company / Group')
    company_director = fields.Char(string='Company Director')
    tax_id = fields.Char(string='TAX ID')
    vat_code = fields.Char(string='VAT')
    id_pkp = fields.Boolean(string='ID PKP')
    iso_certified = fields.Char(string='ISO Certified')
    iso_certificate = fields.Char(string='ISO Certificate')
    fax = fields.Char(string='Fax')
    commodity_id = fields.Many2one('ktc.commodity.group.code', string='Commodity Group Code')
    supp_prod_class_id = fields.Many2one('ktc.supplier.product.classification', string='Supplier Product Classification')
    business_reference_ids = fields.One2many(comodel_name='ktc.business.reference', inverse_name='vendor_id', string='Business Reference')
    turn_on_per_year = fields.Monetary('Turn on Per Year')
    payment_method_id = fields.Many2one('account.payment.method', string='Payment Method')
    credit_limit_value = fields.Monetary('Credit Limit Value')
    nib = fields.Char(string='NIB')
    certificate = fields.Char(string='Certificate')
    business_line = fields.Char(string='Business Line')
    
    
    