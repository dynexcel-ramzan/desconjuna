# -*- coding: utf-8 -*-
{
    'name': "Monthly Processing Report",

    'summary': """
        Customer Invoice Information in given data range from wizard


        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "dynaxel",
    'website': "http://www.dynaxel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [

        # 'report/de_employee_attendance_header.xml',
        'security/ir.model.access.csv',
        'wizard/customer_invoice_wizard_view.xml',
        'report/account_invoice_template.xml',
        'report/account_invoice_view.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installation': True,
    'auto_install': False,
}
