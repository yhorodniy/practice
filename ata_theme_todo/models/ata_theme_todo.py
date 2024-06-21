from odoo import models


class Themetodo(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_todo_post_copy(self, mod):
        self.enable_view('website.template_footer_minimalist')
