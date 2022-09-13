from odoo import fields, models

class Exam(models.Model):
    _name = 'syahriracademy.exam'
    _description = 'Exam information.'

    exam_id = fields.Char(string='Exam ID')
    student_count = fields.Integer(string='Student Count', required=True)
    exam_date = fields.Date(string='Exam Date')

    name = fields.Many2one('syahriracademy.course', string='Course/Exam Name')
    invigilator_id = fields.Many2one('syahriracademy.teacher', string='Invigilator Name')

    _sql_constraints = [
        ('no_nota_unik','unique(exam_id)','ID Exam Tidak Boleh Sama !!!')
    ]