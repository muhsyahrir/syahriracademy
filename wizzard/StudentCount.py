from odoo import api, fields, models


class studentcount(models.TransientModel):
    _name = 'syahriracademy.studentcount'

    exam_id = fields.Many2one('syahriracademy.exam', string='Exam Name', required=True)
    amount = fields.Integer(string='Amount', required=False)
    def button_student_count(self):
        for rec in self:
            self.env['syahriracademy.exam'].search([('id', '=', rec.exam_id.id)]).write({'student_count' : rec.exam_id.student_count + rec.amount})

        