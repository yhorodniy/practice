{
    'name': 'ToDo Theme',
    'description': 'ToDo Theme',
    'category': 'Theme/Services',
    'summary': 'Services',
    'sequence': 300,
    'version': '1.0.4',
    'author': 'iT.Artel',
    'depends': ['theme_common'],
    'data': [
        'data/ir_asset.xml',
        'views/images.xml',
        'views/customizations.xml',
        'views/header.xml',
        'views/footer.xml',
        'views/homepage.xml'
    ],
    'images': [
        'static/description/todo_description.png',
        'static/description/todo_screenshot.png',
    ],
    'images_preview_theme': {
        'website.s_cover_default_image': '/ata_theme_todo/static/src/img/snippets/s_cover.jpg',
        'website.s_text_image_default_image': '/ata_theme_todo/static/src/img/snippets/s_text_image.jpg',
        'website.s_masonry_block_default_image_1': '/ata_theme_todo/static/src/img/snippets/s_masonry_block.jpg',
        'website.s_image_text_default_image': '/ata_theme_todo/static/src/img/snippets/s_image_text.jpg',
        'website.s_parallax_default_image': '/ata_theme_todo/static/src/img/snippets/s_parallax.jpg',
        'website.s_picture_default_image': '/ata_theme_todo/static/src/img/snippets/s_picture.jpg',
    },
    'snippet_lists': {
        'homepage': ['s_cover', 's_text_image', 's_image_text', 's_picture', 's_masonry_block', 's_call_to_action'],
    },
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-todo.odoo.com',
    'assets': {
        'website.assets_editor': [
            'ata_theme_todo/static/src/js/tour.js',
        ],
        'web.assets_frontend': [
            'ata_theme_todo/static/src/scss/theme.scss',
            'ata_theme_todo/static/src/font/stylesheet.css',
            'ata_theme_todo/static/src/js/swiper-bundle.min.js',
            'ata_theme_todo/static/src/css/swiper-bundle.min.css',
            'ata_theme_todo/static/src/js/home.js',
        ],
        'web._assets_primary_variables': [
            "ata_theme_todo/static/src/scss/primary_variables.scss",
        ]
    }
}
