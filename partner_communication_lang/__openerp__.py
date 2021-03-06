# -*- coding: utf-8 -*-

# Copyright 2018 Rémy Taymans <remytaymans@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Partner Communication Language',

    'summary': """
    Let you add configurable languages to contacts.
    """,
    'description': """
    """,

    'author': 'Coop IT Easy, Rémy Taymans',
    'license': 'AGPL-3',
    'version': '9.0.1.0',
    'website': "https://coopiteasy.be",

    'category': 'Partner Management',

    'depends': [
        'base',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/partner.xml',
        'views/partner_communication_lang.xml',
    ]
}
