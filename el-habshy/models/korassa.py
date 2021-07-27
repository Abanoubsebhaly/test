
from odoo import api, fields, models


class korass_elshorot(models.Model):
    _name = "elhabshy.korass_elshorot"
    _description = "كراسة الشروط"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Famele'),
        ('other', 'Other'),
    ], required=True, default='male',)
    Test = fields.Integer(string='test')
    note=fields.Text(string='Note')
    customar=fields.Many2one('res.partner',string="Responsible")