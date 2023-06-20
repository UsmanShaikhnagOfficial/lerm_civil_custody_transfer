from odoo import api, fields, models
from odoo.exceptions import UserError

class Srf(models.Model):
    _inherit = "lerm.civil.srf"

    state = fields.Selection([
        ('1-draft', 'Draft'),
        ('2-onsite', 'OnSite'),
        ('3-transit', 'In Transit'),
        ('4-received', 'Received at Lab'),
        ('5-confirm', 'Confirmed')
    ], string='State', default='1-draft')