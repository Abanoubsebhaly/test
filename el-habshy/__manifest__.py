# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'El-habshy ',
    'version': '1.0',
    'category': 'AAA',
    'summary': 'my first module',
    'description': 'discriptino',
    
    'sequence':6,
    'depends': ['base'],
    'data': [
     'security/ir.model.access.csv',
     'views/korassa.xml'
    ],
    'installable': True,
    'application':True,
    'auto_install': False
}
