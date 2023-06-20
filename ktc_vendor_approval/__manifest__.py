# -*- coding: utf-8 -*-
{
    'name': "ktc_vendor_approval",
    'summary': """[KTC] Vendor Approval""",
    'description': """[KTC] Vendor Approval""",
    'author': "KTC",
    # 'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','winprof_approval','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/ktc_res_partner.xml',
    ],
}
