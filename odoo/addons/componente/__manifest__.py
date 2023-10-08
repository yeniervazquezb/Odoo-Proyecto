# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Componente',
    'version': '1.0',
    'author': 'Yenier Vazquez Banos',
    'category': 'Sales/CRM',
    'website': 'https://www.odoo.com/app/crm',
    'depends': [
        'base_setup',
        'sales_team',
        'mail',
        'calendar',
        'resource',
        'utm',
        'web_tour',
        'web_kanban_gauge',
        'contacts',
        'digest',
        'phone_validation',
    ],
'description': """
Módulo de Odoo que permita administrar componentes de software.
========================================
    """,
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
