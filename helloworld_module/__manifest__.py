{
    'name': 'Hello World Website',
    'version': '1.0.0',
    'author': 'Your Name',
    'description': 'My custom website for Odoo',
    'category': 'Website',
    'depends': ['website', 'snippets_library', 'base'],
    'data': [
        'views/head.xml',
        'views/snippets/homepage/s_homepage_first_section.xml',
        'views/snippets/homepage/s_homepage_second_section.xml',
        'views/snippets/homepage/s_homepage_third_section.xml',
        'views/homepage.xml',


        # 'views/snippets/s_text_image.xml',
        
        # 'views/snippets/s_first_section.xml',
        # 'views/snippets/s_third_section.xml',
        # 'views/snippets/s_fifth_section.xml',
        # 'views/snippets/s_sixth_section.xml',
        # 'views/templates.xml',

        # 'data/website_data.xml',
        # 'data/page_data.xml',
        # 'data/menu_data.xml',

        # 'views/module_views/hellowolrd_views.xml',
        # 'views/module_views/helloworld_menu.xml',
        # 'views/module_views/helloworld_property_kanban.xml',
        # 'views/module_views/helloworld_property_view.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'helloworld_module/static/src/scss/theme_style.scss',
            'helloworld_module/static/src/scss/style.scss',
            'helloworld_module/static/src/scss/accordion_style.scss',
            'helloworld_module/static/src/js/accordion.js',
            'helloworld_module/static/src/scss/mainpage.scss',
            'helloworld_module/static/src/scss/index.scss',
        ],
        'web._assets_frontend_helpers': [
            ('prepend', 'helloworld_module/static/src/scss/bootstrap_overridden.scss'),
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}