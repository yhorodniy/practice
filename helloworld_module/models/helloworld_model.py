from odoo import fields, models


class HelloWorld(models.Model):
    _name = 'helloworld.module'
    _description = 'Hello World Module'

    title = fields.Char(string='Title', default='Hello World')