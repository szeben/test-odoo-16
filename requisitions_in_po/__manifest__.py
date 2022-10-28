# -*- coding: utf-8 -*-
{
    'name': "Relación de Ordenes de compras con requisiciones",

    'summary': """
        Permite enlazar una Orden de Compra con una o varias Requisiciones.""",

    'description': """
        Permite enlazar una Orden de Compra con una o varias Requisiciones.
category_id: Compras.
    """,

    'author': "Techne Studio IT & Consulting",
    'website': "https://technestudioit.com/",

    'license': "Other proprietary",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Account',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'sale_management'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
