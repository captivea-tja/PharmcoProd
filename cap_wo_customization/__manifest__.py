# -*- coding: utf-8 -*-
{
    'name': "Cap WorkOrder Customizations",

    'summary': """
    	Will describe Operation description on work order.
    	Will allow to finish the process of Wordorder only if confirmed by two users.
        """,

    'description': """
        """,

    'author': 'Captivea',
    'website': 'www.captivea.us',
    'version': '13.0.1.0.0',
    'category': 'Manufacturing/Manufacturing',

    # any module necessary for this one to work correctly
    'depends': ['cap_multiple_workorder_component', 'cap_mrp_customization'],

    # always loaded
    'data': [
        'views/mrp_workorder_views.xml',
    ],

}
