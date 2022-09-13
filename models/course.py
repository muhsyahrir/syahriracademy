from odoo import models, fields

class Courses(models.Model):
    _name = 'syahriracademy.course'
    _description = 'Here Course information is stored.'

    name = fields.Char(string='Course Name')
    course_code = fields.Char(string='Course Code')
    course_description = fields.Text(string='Course Description')
    source_price = fields.Integer(string='Source Price', required=True)
    credit_hour = fields.Integer(string='Credit')
    department_id = fields.Many2one('syahriracademy.departement', string='Department')
    color = fields.Integer()

    