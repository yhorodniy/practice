

from odoo import fields, models


class HWPage(models.Model):
    _name = 'hw.page'

    name = fields.Char(string="Page name")