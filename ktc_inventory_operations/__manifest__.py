# -*- coding: utf-8 -*-
{
    'name': "ktc_inventory_operations",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'maintenance', 'stock_landed_costs', 'ktc_inventory_products'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/inventory_adjustment_views.xml',
        'views/stock_scrap_views.xml',
        'views/salvaged_material_views.xml',
        'views/landed_costs_views.xml',
        'views/stock_picking_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "license": "AGPL-3",
    "installable": True,
    "application": True,
}
