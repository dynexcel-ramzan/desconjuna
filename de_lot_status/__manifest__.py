# -*- coding: utf-8 -*-
{
    'name': "Lot Status",

    'summary': """
    Lots Status Report
        """,

    'description': """
        Lot Status Report
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','mrp'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/stock_production_lot_views.xml',
        'report/stock_move_lot_report_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}