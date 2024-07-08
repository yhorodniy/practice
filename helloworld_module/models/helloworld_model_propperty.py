from odoo import fields, models


class HelloworldProperty(models.Model):
    _name = "helloworld.property"
    _description = "helloworld.module.property"

    name = fields.Char(string="Property name", required=True)
    value = fields.Char(string="Property value", required=True)
    module_id = fields.Many2one('helloworld.module', string="Module")