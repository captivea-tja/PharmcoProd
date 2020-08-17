from odoo import api, fields, models, _
from odoo.tools import float_compare, float_round
from odoo.exceptions import ValidationError



class MrpProductionWorkcenterLine(models.Model):
    _inherit = 'mrp.workorder'

    operation_note = fields.Text('Description', related='operation_id.note')
    user_ids = fields.Many2many('res.users', string='WO Approved By')

    def do_finish(self):
    	current_user = self.env.user.id
    	if not self.user_ids:
    		self.user_ids = [(4, current_user)]
    	elif self.user_ids and current_user in self.user_ids.ids:
    		raise ValidationError(_("You already confirmed the WO. Another person " \
    			"will be able to complete this process"))
    	elif self.user_ids and len(self.user_ids) < 2 and current_user not in self.user_ids.ids:
    		self.user_ids = [(4, current_user)]
    		if len(self.user_ids) >= 2:
    			return super(MrpProductionWorkcenterLine, self).do_finish()
    	elif self.user_ids and len(self.user_ids) >= 2:
    		return super(MrpProductionWorkcenterLine, self).do_finish()
