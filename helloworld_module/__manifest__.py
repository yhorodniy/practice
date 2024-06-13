{
    'name': 'Hello World Website',
    'version': '1.0.0',
    'author': 'Your Name',
    'description': 'My custom website for Odoo',
    'category': 'Website',
    'depends': ['website'],
    'data': [
        'views/fourth_section_view.xml',
        'views/templates.xml',
        'data/website_data.xml',
        'data/page_data.xml',
        'data/menu_data.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'helloworld_module/static/src/scss/style.scss'
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}