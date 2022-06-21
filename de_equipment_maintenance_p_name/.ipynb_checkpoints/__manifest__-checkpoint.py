# -*- coding: utf-8 -*-
{
    'name': "Equipment parent name include with name",

    'summary': """
             Equipment parent name include with name
             1-Many2one name field include with category_id field
             """,

    'description': """
            Equipment parent name include with name
             1-Many2one name field include with category_id field
             in default name field show in many2one field we also include category_id
             field with name field
             """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','maintenance','stock','account'],

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
