from odoo import fields, models

class mahasiswa (models.Model):
	_name = "mahasiswa"
	_description = "Mahasiswa"
	
	image = fields.Binary()
	name = fields.Char(string="Nama")
	code = fields.Char(string="NIM")
	tgl_sidang = fields.Date(string="Tanggal Sidang")
	state = fields.Selection([
		('waiting', 'Waiting'),
		('success', 'Success'),
		('fail', 'Fail'),
	], default='waiting', string='status')

	def button_success(self):
		self.state='success'

	def button_fail(self):
		self.state='fail'