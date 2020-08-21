# -*- coding: utf-8 -*-
{
    'name': "Cap Quality Customizations",

    'summary': """
        This module customises Qualty Alert and will allow two user 
        validation to confirm it by prompting wizard to add password""",

    'description': """
        This module customises Qualty Alert and will allow two user 
        validation to confirm it by prompting wizard to add password""",

    'author': 'Captivea',
    'website': 'www.captivea.us',
    'version': '13.0.1.0.0',
    'category': 'Manufacturing/Quality',

    # any module necessary for this one to work correctly
    'depends': ['quality_control'],

    # always loaded
    'data': [
        'security/quality_security.xml',
        'wizard/password_confirmation_views.xml',
        'views/quality_alert_views.xml',
    ],

}
