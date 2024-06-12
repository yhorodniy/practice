{
    'name': 'Hello World Website',
    'version': '1.0.0',
    'author': 'Your Name',
    'description': 'My custom website for Odoo',
    'category': 'Website',
    'depends': ['website'],
    'data': [
        'views/templates.xml',
        # 'data/configurator_data.xml',
        'data/website_data.xml',
        'data/page_data.xml',
        'data/menu_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}