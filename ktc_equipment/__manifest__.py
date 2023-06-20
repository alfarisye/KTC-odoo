# -*- coding: utf-8 -*-
{
    'name': "ktc_equipment",
    'license': 'Other proprietary',
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "anggakawa",
    'website': "https://www.hasnurgroup.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'ktc_maintenance_master_data', 'ktc_inventory_master_data'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/equipment_master_view.xml',
        'views/meter_reading_view.xml',
        'views/register_equipment_view.xml',
        'views/service_type_view.xml',
        'views/service_package_view.xml',
        'views/standard_tasklist_view.xml',
        'views/tyre_form_view.xml',
        'views/swapping_component_view.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
