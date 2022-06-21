# -*- coding: utf-8 -*-
{
    'name': "Picking Owner",

    'summary': """
        Picking Owner Mandatory
        """,

    'description': """
        This module will make owner field mandatory on required picking type
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Warehouse',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','to_stock_picking_validate_manual_time'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}