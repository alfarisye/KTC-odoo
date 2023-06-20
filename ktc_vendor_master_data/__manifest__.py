# -*- coding: utf-8 -*-
{
    'name': "ktc_vendor_master_data",
    'summary': """[KTC] Vendor Master Data""",
    'description': """[KTC] Vendor Master Data""",
    'author': "KTC",
    # 'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/ktc_commodity_group_code.xml',
        'views/ktc_supplier_product_classification.xml',
        'views/ktc_res_partner.xml',
    ],
}
