from odoo import fields, models

class Teacher(models.Model):
    _name = 'syahriracademy.teacher'
    _description = 'Teacher information.'

    name = fields.Char(string='Teacher Name')
    teacher_id = fields.Char(string='Teacher ID')
    teacher_phone = fields.Char(string='Phone Number')
    teacher_email = fields.Char(string='Email Address')
    teacher_photo = fields.Binary(string="Photo", attachment=True)

    course_ids = fields.Many2many('syahriracademy.course',string='Courses')
    department_id = fields.Many2one('syahriracademy.departement', string='Department')

    _sql_constraints = [
        ('no_nota_unik','unique(teacher_id )','ID Teacher Tidak Boleh Sama !!!')
    ]