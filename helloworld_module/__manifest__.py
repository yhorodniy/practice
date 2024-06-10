# {
#     'name': 'Hello World Module',
#     'version': '1.0',
#     'author': 'Your Name',
#     'depends': ['base', 'website'],
#     'data': [
#         # 'security/ir.model.access.csv',
#         # 'views/hello_world_view.xml',
#         'data/menu_data.xml',
#         'data/page_data.xml',
#         'data/website_data.xml',
#     ],
#     'demo': [],
#     'installable': True,
#     'application': True,
# }

{
    'name': 'Hello World Module',
    'version': '1.0.0',
    'category': 'Website',
    'depends': ['website'],
    'data': [
        'data/website_data.xml',
        # 'data/page_data.xml',
        # 'data/menu_data.xml',
    ],
    'application': True,
}