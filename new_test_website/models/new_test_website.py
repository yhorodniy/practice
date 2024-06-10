from odoo import models, fields


class NewTestWebsite(models.Model):
    _inherit = 'website'

    name = fields.Char(string='Title')