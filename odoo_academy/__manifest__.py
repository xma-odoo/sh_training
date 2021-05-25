# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    'summary': """Academy app to manage TRaining""",
    'description': """
        Aademy MOdule to manage Training:
        - Courses
        - Sessions
        - Attendees
    """,
    'author': 'Odoo',
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'views/academy_menuitems.xml',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
}
