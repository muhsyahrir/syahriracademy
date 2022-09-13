from odoo import models, fields
class PartnerXlsx(models.AbstractModel):
    _name = 'report.syahriracademy.report_transaksisource_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, transaksisource):
        sheet = workbook.add_worksheet('Daftar Transaksi Source')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'No. Transaksi')
        sheet.write(1, 1, 'Tgl. Transaksi')
        sheet.write(1, 2, 'Student Name')
        sheet.write(1, 3, 'Total Bayar')
        row = 2
        col = 0
        for obj in transaksisource:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, str(obj.tgl_pembelian))
            sheet.write(row, col+3, obj.total_bayar)
            for brg in obj.student_ids:
                sheet.write(row, col+2, brg.name)
                col += 1
            row += 1