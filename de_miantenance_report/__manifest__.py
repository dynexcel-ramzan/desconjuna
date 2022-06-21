# -*- coding: utf-8 -*-
{
    'name': "Maintenance Report",

    'summary': """
                Maintenance Report Piviot View
                """,

    'description': """
        Maintenance Report Piviot View
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",

    'category': 'Maintenance',
    'version': '14.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['maintenance'],

    # always loaded
    'data': [
        'views/purchase_report_view.xml',
        # 'report/sale_gain_report_template.xml',
    ],

}
