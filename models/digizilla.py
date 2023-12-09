from odoo import fields, models
# from odoo.exceptions import UserError

class DigizillaUser(models.Model):
    _name = "digizilla.user"

    name = fields.Char(string="User Name", required=True)
    email = fields.Char(string="User Email")
    phone = fields.Char(string="User Phone")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    country = fields.Char()
    joining_date = fields.Date()
    tags = fields.Char()
    customers = fields.Many2many('res.partner', string='Customers')
    company = fields.Many2one('res.company', string='Company', required=True)
    notes = fields.Text()
    comments = fields.Char()

