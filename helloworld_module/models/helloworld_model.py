from odoo import fields, models


class HelloWorld(models.Model):
    _name = 'helloworld.module'
    _description = 'Hello World Module'

    name = fields.Char(string='Section name', required=True)
    properties_ids = fields.One2many('helloworld.property', 'module_id', string="Properties")