from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Transaksisource(models.Model):
    _name = 'syahriracademy.transaksisource'
    _description = 'New Description'
    
    color = fields.Integer()
    name = fields.Char(string='No. Transaksi')
    student_ids = fields.Many2many('syahriracademy.student', string='Student Name')
    tgl_pembelian = fields.Datetime(string='Tgl. Transaksi', default=fields.Datetime.now())
    total_bayar = fields.Integer(compute='_compute_totalbayar', string='Total Pembayaran')
    detailsource_ids = fields.One2many(comodel_name='syahriracademy.detailsource', inverse_name='transaksi_id', string='Detail Source')

    state = fields.Selection(
        string='Status',
        selection=[('draft', 'Draft'),
                    ('confirm', 'Confirm'),
                    ('done', 'Done'),
                    ('cancelled', 'Cancelled'),
                    ],
        required=True, readonly=True, default='draft')
    
    def action_confirm(self):
        self.write({'state': 'confirm'})
    
    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_draft(self):
        self.write({'state': 'draft'})

    @api.depends('detailsource_ids')
    def _compute_totalbayar(self):
        for rec in self:
            a = sum(self.env['syahriracademy.detailsource'].search([('transaksi_id', '=', rec.id)]).mapped('subtotal'))
            rec.total_bayar = a

    
     #odoo14
    def unlink(self):
        if self.filtered(lambda line: line.state != 'draft'):
                raise ValidationError("Tidak dapat menghapus jika status BUKAN DRAFT!!")
        else:
            if self.detailsource_ids:
                a=[]
                for rec in self:
                    a = self.env['syahriracademy.detailsource'].search([('transaksi_id', '=', rec.id)])
                    print(a)
                for ob in a:
                    print(str(ob.source_id.name) + ' ' + str(ob.qty))
                    ob.source_id.credit_hour += ob.qty
        record = super(Transaksisource,self).unlink()

    def write(self,vals):
        for rec in self:
            a = self.env['syahriracademy.detailsource'].search([('transaksi_id','=',rec.id)])
            print(a)
            for data in a:
                print(str(data.source_id.name)+' '+str(data.qty)+' '+str(data.source_id.credit_hour))
                data.source_id.credit_hour += data.qty
        record = super(Transaksisource,self).write(vals)
        for rec in self:
            b = self.env['syahriracademy.detailsource'].search([('transaksi_id','=',rec.id)])
            print(a)
            print(b)
            for databaru in b:
                if databaru in a:
                    print(str(databaru.source_id.name)+' '+str(databaru.qty)+' '+str(databaru.source_id.credit_hour))
                    databaru.source_id.credit_hour -= databaru.qty
                else:
                    pass
        return record


class DetailSource(models.Model):
    _name = 'syahriracademy.detailsource'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    transaksi_id = fields.Many2one(comodel_name='syahriracademy.transaksisource', string='Detail Source')
    source_id = fields.Many2one(comodel_name='syahriracademy.course', string='List Source')
    harga_satuan = fields.Integer(string='Harga Satuan')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')
    
    @api.depends('harga_satuan', 'qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.qty * rec.harga_satuan


    @api.onchange('source_id')
    def _onchange_source_id(self):
        if(self.source_id.source_price):
            self.harga_satuan = self.source_id.source_price

    @api.model
    def create(self,vals):      
        record = super(DetailSource,self).create(vals)
        if record.qty:
            self.env['syahriracademy.course'].search([('id', '=', record.source_id.id)]).write({'credit_hour' : record.source_id.credit_hour - record.qty})
        return record

    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty <1:
                raise ValidationError("Mau belanja {} berapa banyak yah..".format(rec.source_id.name))
            elif (rec.source_id.credit_hour < rec.qty):
                raise ValidationError('Creadit Hour {} tidak mencukupi, hanya tersedia {}'.format(rec.source_id.name,rec.source_id.credit_hour))
    

    