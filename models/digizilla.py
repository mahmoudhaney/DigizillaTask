from odoo import fields, models

class DigizillaUser(models.Model):
    _name = "digizilla.user"
    _description = 'Digizilla Model'
    _inherit = ["mail.thread"]

    name = fields.Char(string="User Name", required=True, tracking=True)
    email = fields.Char(string="User Email", tracking=True)
    phone = fields.Char(string="User Phone", tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], tracking=True)
    country = fields.Char(tracking=True)
    joining_date = fields.Date(tracking=True)
    tags = fields.Char(tracking=True)
    customers = fields.Many2many('res.partner', string='Customers', tracking=True)
    company = fields.Many2one('res.company', string='Company', required=True, tracking=True)
    notes = fields.Text(tracking=True)
    comments = fields.Char(tracking=True)
