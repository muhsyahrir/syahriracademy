from odoo import models, fields
class PartnerXlsx(models.AbstractModel):
    _name = 'report.syahriracademy.report_exam_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, exam):
        sheet = workbook.add_worksheet('Daftar Exam')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'Course/Exam Name')
        sheet.write(1, 1, 'Exam ID')
        sheet.write(1, 2, 'Student Cout')
        sheet.write(1, 3, 'Invigilator Name')
        sheet.write(1, 4, 'Exam Date')
        row = 2
        col = 0
        for obj in exam:
            col = 0
            sheet.write(row, col+1, obj.exam_id)
            sheet.write(row, col+2, obj.student_count)
            sheet.write(row, col+4, str(obj.exam_date))
            for brg in obj.name:
                sheet.write(row, col, brg.name)
                col += 1
                for brg in obj.invigilator_id:
                    sheet.write(row, col+2, brg.name)
                    col += 1
            row += 1