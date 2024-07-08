{
    'name': 'Custom Snippets Library',
    'version': '1.0.0',
    'description': 'My custom snippets for websites',
    'category': 'Website',
    'depends': ['website'],
    'data': [
        'views/snippets.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_frontend': [
            
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}