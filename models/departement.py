from odoo import api, fields, models


class Departement(models.Model):
    _name = 'syahriracademy.departement'
    _description = 'New Description'

    name = fields.Char(string='Department Name')
    budget = fields.Float(string='Department Budget')
   
    engr_dept = fields.Boolean(string='Engineering Department')

    student_ids = fields.One2many('syahriracademy.student', 'department_id', string='Student List')
    course_ids = fields.One2many('syahriracademy.course', 'department_id', string='Course List')
    teacher_ids = fields.One2many('syahriracademy.teacher', 'department_id', string='Teacher List')