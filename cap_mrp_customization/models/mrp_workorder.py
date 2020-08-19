from odoo import api, fields, models, _
from odoo.tools import float_compare, float_round
from odoo.exceptions import UserError
import datetime

class MrpProductionWorkcenterLine(models.Model):
    _inherit = 'mrp.workorder'

    def do_finish(self):
        res = super(MrpProductionWorkcenterLine, self).do_finish()
        finished_lines = self.production_id.finished_move_line_ids or self.production_id.move_finished_ids.mapped('move_line_ids')
        for line in finished_lines:
            if line.lot_id:
                line.lot_id.manufacturer_lot = self.production_id.manufacturer_lot
                line.lot_id.tare_weight = self.production_id.tare_weight
                line.lot_id.gross_weight = self.production_id.gross_weight
                line.lot_id.component_weight = self.production_id.component_weight
                line.lot_id.container_type = self.production_id.container_type
                line.lot_id.supplier_lot = self.production_id.supplier_lot
                line.lot_id.supplier_id = self.production_id.supplier_id.id
                # line.lot_id.manufacturer_date = datetime.datetime.now().date()
        return res