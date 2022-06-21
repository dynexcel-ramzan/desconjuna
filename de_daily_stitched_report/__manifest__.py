{
    "name": "Daily Greige Stitch Report",
    "category": 'Stock',
    "summary": 'Print Greige Stitch Information according to date range select on wizard',
    "description": """Generate Report from Stock Move Line""",
    "sequence": 0,
    "author": "Dynexcel",
    "website": "http://www.dynexcel.co",
    "version": '12.0.0.0',
    "depends": ['base', 'stock'],
    "data": [
        'security/ir.model.access.csv',
        'wizards/stock_transfer_wizard.xml',
        'views/stock_transfer_view.xml',
        'report/production_report.xml',
    ],
    "price": 25,
    "currency": 'PKR',
    "installable": True,
    "application": True,
    "auto_install": False,
}
