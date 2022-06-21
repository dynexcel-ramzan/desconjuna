from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # @api.multi
    def button_validate(self):
        self.ensure_one()
        if not self._context.get('manual_validate_date_time') and self.env.user.has_group('to_backdate.group_backdate'):
            if self.picking_type_id.is_owner == True and not self.owner_id:
                    raise UserError(_('Owner is not assigned'))
            else:
                view = self.env.ref('to_stock_picking_validate_manual_time.view_validate_datetime_manual')
                ctx = dict(self._context or {})
                ctx.update({'default_picking_id': self.id})
                return {
                    'type': 'ir.actions.act_window',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'stock.picking.validate.manual.datetime.wizard',
                    'views': [(view.id, 'form')],
                    'view_id': view.id,
                    'target': 'new',
                    'context': ctx,
                }
        return super(StockPicking, self).button_validate()

    # @api.multi
    def _action_done(self):
        res = super(StockPicking, self)._action_done()
        manual_validate_date_time = self._context.get('manual_validate_date_time', False)
        if manual_validate_date_time:
            self.filtered(lambda x: x.state == 'done').write({'date_done': manual_validate_date_time})
        return res
