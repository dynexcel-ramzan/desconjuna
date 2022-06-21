# -*- coding: utf-8 -*-
{
    'name': "SO Processing Report",

    'summary': """
                Sale Order Processing Report
                """,

    'description': """
        Sale Order Processing Report
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",

    'category': 'Sales',
    'version': '12.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mrp', 'sale','purchase','account','product','sale'],

    # always loaded
    'data': [
        'report/sale_gain_report.xml',
        'report/sale_gain_report_template.xml',        
    ],

}
