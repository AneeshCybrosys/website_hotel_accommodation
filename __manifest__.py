# -*- coding: utf-8 -*-
{
    'name': "Website Hotel Accommodation",

    'summary': """
        Adds a menu hotel accommodation""",

    'description': """
        Description
    """,

    'author': "Minions 6",

    'version': '15.0.1.0',
    'depends': ['website', 'hotel_room_management'],

    'data': [
        'views/website_accommodation_menu.xml',
        'views/accommodation_form_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'website_hotel_accommodation/static/src/js/accommodation.js',
        ]
    }
}
