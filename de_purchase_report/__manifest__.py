# -*- coding: utf-8 -*-
{
    'name': "Add PO number, Source document and price unit in purchase report",

    'summary': """
                Add PO number, Source document and price unit in purchase report
                """,

    'description': """
        Add Purchase order number in purchase analysis report
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",

    'category': 'Sales',
    'version': '12.0.0.',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

    # always loaded
    'data': [
        'views/purchase_report_view.xml',
        # 'report/sale_gain_report_template.xml',
    ],

}
