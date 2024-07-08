from odoo import api, fields, models

class Test(models.Model):
    _name = 'test.model'
    _description = 'Test Model'

    name = fields.Char(string='Title')
    first_num = fields.Integer(string='First Number', default=5)
    second_num = fields.Integer(string='Second Number', default=11)
    operation_type = fields.Selection(
        string='Operation Type',
        selection=[
            ('sum', 'Summ'),
            ('subtr', 'Subtracting'),
            ('mult', 'Multiply')
        ],
        required=True,
        copy=False,
        default='sum',
    )
    sum_num = fields.Integer(string="Sum numbers", compute='_compute_sum')
    subtracting_num = fields.Integer(string="Subtracting numbers", compute='_compute_subtracting')
    multiply_num = fields.Integer(string="Multiply numbers", compute='_compute_multiply')

    @api.depends('first_num', 'second_num')
    def _compute_sum(self):
        for el in self:
            el.sum_num = el.first_num + el.second_num

    @api.depends('first_num', 'second_num')
    def _compute_subtracting(self):
        for el in self:
            el.subtracting_num = el.first_num - el.second_num

    @api.depends('first_num', 'second_num')
    def _compute_multiply(self):
        for el in self:
            el.multiply_num = el.first_num * el.second_num