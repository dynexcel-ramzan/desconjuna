# -*- coding: utf-8 -*-
{
    'name': "Add Saleperson Field",

    'summary': """
        This module add new saleperson field in contacts, sale and invoice""",

    'description': """
        This module add new saleperson field in contacts, sale and invoice
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Contacts',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'account', 'sale', 'sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_move_view.xml',
        'views/res_partner.xml',
        'views/sale_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
