from odoo import fields, models

class AcademyStudent(models.Model):
    _name = 'syahriracademy.student'
    _description = 'Student information.'

    color = fields.Integer()
    name = fields.Char(string='Student Name')
    student_id = fields.Char(string='Student ID')
    student_phone = fields.Char(string='Phone Number')
    student_email = fields.Char(string='Email Address')
    student_photo = fields.Binary(string="Photo", attachment=True)
    student_dob = fields.Date(string="Date of Birth")
    course_ids = fields.Many2many('syahriracademy.course', string='Courses')
    department_id = fields.Many2one('syahriracademy.departement', string='Department')

    _sql_constraints = [
        ('no_nota_unik','unique(student_id)','ID Student Tidak Boleh Sama !!!')
    ]