# -*- coding: utf-8 -*-
{
    'name': 'Payment Approval',
    'version': '14.0.1',
    'category': 'Accounting',
    'description': """
""",
    'depends': [
        'base',
        'account',
    ],
    'data': [
#         'security/ir.model.access.csv',
        'account_user.xml',
        'account_payment_view.xml',
    ],
    'application': False,
    'license': 'OPL-1',
}
