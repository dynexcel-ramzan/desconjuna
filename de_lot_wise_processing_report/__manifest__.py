# -*- coding: utf-8 -*-
{
    'name': "Lot Wise Processing Report",

    'summary': """
        Owner and Lot wise greig stock status. Gregie Received, processed and fold information


        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Stock',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [

        # 'report/de_employee_attendance_header.xml',
        'security/ir.model.access.csv',
        'wizard/invoice_customer_wizard_view.xml',
        'report/invoice_customer_wizard_report_template.xml',
        'report/invoice_customer_wizard_report_view.xml',
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
