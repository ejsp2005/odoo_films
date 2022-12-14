# -*- coding: utf-8 -*-
{
    'name': "Films",

    'summary': """
        This is a small plugin about films
    """,

    'description': """
        This is a small plugin about films
    """,

    'author': "Ernesto J. Suárez Pons",
    'website': "http://www.films.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '0.1',
    'license': 'LGPL-3',
    'category': 'Entertainment',

    'depends': ['base'],

    # always loaded
    'data': [
        'views/film.list.views.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
    ],
    
    'auto_install': False,
    'application': True,
}
