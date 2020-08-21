# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PasswordConfirmation(models.TransientModel):
    _name = "password.confirmation"

    user_login = fields.Char(string='Login')
    user_password = fields.Char(string='Password')
    quality_alert_id = fields.Many2one('quality.alert', string='Quality Alert')

    def action_validate(self):
        if self.user_login and self.user_password:
            user = self.env['res.users'].search(
                [('login', '=', self.user_login)])
            if user:
                user._check_credentials(self.user_password)
                if self.quality_alert_id:
                    return self.quality_alert_id.do_confirm(user)
