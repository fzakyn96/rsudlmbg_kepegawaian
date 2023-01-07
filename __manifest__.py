# -*- coding: utf-8 -*-
{
    'name': "Modul Kepegawaian",

    'summary': """
       Modul kepegawaian RSUD Lembang""",

    'description': """
       Modul kepegawaian RSUD Lembang adalah modul yang di tujukan untuk pengelolaan data internal kepegawaian RSUD Lembang
    """,

    'author': "fzakyn",
    'website': "https://www.rsudlembang.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Modul Internal Instansi Pemerintahan',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/views.xml',
        'views/actions.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
