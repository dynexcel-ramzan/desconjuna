# -*- coding: utf-8 -*-
{
    'name': "Sale Invoice Commissions",

    'summary': """
        Sale Invoice Commissions
        """,

    'description': """
        Sale Invoice Commissions
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '12.0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
            'de_sale_comission'],

    # always loaded
    'data': [
          #'data/invoice_server_action.xml',
          #'security/security.xml',
          #'security/ir.model.access.csv',
          #'views/invoice_commission_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
#         'demo/demo.xml',
    ],
}



