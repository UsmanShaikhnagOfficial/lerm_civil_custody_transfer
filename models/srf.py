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