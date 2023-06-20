# -*- coding: utf-8 -*-
{
    'name': "ktc_purchase_request_approval",
    'summary': """[KTC] Purchase Request Approval""",
    'description': """[KTC] Purchase Request Approval""",
    'author': "KTC",
    # 'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase_request','winprof_approval'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/ktc_purchase_request.xml',
    ],
}
