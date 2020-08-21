# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, _
from odoo.exceptions import ValidationError


class QualityAlert(models.Model):
    _inherit = "quality.alert"

    user_ids = fields.Many2many("res.users", string="Approved By")
    validate_visible = fields.Boolean(string="Validate Visible?",
                                      compute="_compute_validate_visible")

    def _compute_validate_visible(self):
        done_state = self.env['quality.alert.stage'].search(
            [('done', '=', True)])
        for alert in self:
            alert.validate_visible = False
            if alert.stage_id != done_state and self.env.user.has_group(
                    'cap_quality_customization.group_quality_alert_validate'):
                alert.validate_visible = True

    def do_validate(self):
        wizard = self.env['password.confirmation'].create({
            'user_login': self.env.user.login,
            'user_password': '',
            'quality_alert_id': self.id,
        })
        action = self.env.ref(
            'cap_quality_customization.action_password_confirmation').read()[0]
        action.update({
            'res_id': wizard.id,
            'target': 'new'
        })
        return action

    def do_confirm(self, user_id):
        current_user = user_id and user_id.id or self.env.user.id
        stage_id = self.env['quality.alert.stage'].search(
            [('done', '=', True)])
        if self.user_ids and len(self.user_ids) >= 2 and stage_id:
            self.stage_id = stage_id.id
        elif not self.user_ids:
            self.user_ids = [(4, current_user)]
        elif self.user_ids and current_user in self.user_ids.ids:
            raise ValidationError(_("You already confirmed the WO. Another "
                                    "person will be able to complete this "
                                    "process"))
        elif stage_id and self.user_ids and len(self.user_ids) < 2 and \
                current_user not in self.user_ids.ids:
            self.user_ids = [(4, current_user)]
            if len(self.user_ids) >= 2:
                self.stage_id = stage_id.id
