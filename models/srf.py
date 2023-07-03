from odoo import api, fields, models
from odoo.exceptions import UserError

class Srf(models.Model):
    _inherit = "lerm.civil.srf"

    state = fields.Selection([
        ('1-draft', 'Draft'),
        ('2-confirm', 'Confirmed'),
        ('3-onsite', 'OnSite'),
        ('4-transit', 'In Transit'),
        ('5-received', 'Received at Lab')
    ], string='State', default='1-draft')

    sample_picture = fields.Binary(string="Sample Picture")
    sample_picture_name = fields.Char(string="Attachment Name")

    attachment_table = fields.One2many('srf.attachments','srf_id',string="Attachment Table")

    courier_name = fields.Char(string="Courier Name")
    courier_vehicle_no = fields.Char(string="Courier Vehicle No")
    courier_contact_no = fields.Char(string="Courier Contact No")
    courier_description = fields.Char(string="Courier Description")

    latitude = fields.Float(string="Latitude")
    longitute = fields.Float(string="Longitude")






class SrfAttachment(models.Model):
    _name = 'srf.attachments'

    srf_id = fields.Many2one('lerm.civil.srf')
    attachment = fields.Binary(string="Attachment")
    attachment_name = fields.Char(string="Attachment Name")