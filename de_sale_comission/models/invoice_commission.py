from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_agent = fields.Boolean(string='Is a Agent')
    agent_id = fields.Many2one('res.partner', string='Agent', domain="[('is_agent','=',True),('id','!=',id)]")
    comission = fields.Float(string="Pre Defined Commission")

    
class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    agent_id = fields.Many2one(related='partner_id.agent_id')
    

class AccountMoveInherit(models.Model):
    _inherit = 'account.move'
    

    
    @api.model
    def action_create_bill(self):
        for line in self:
            if line.state == 'draft':
                raise UserError(_('Please Select Invoices Other than draft or cancel'))  
            elif line.state == 'cancel':
                raise UserError(_('Please Select Invoices Other than draft or cancel'))     
        agent_list = []
        for invoice in self:
            if invoice.agent_id and invoice.commission_settled == False:
                agent_list.append(invoice.agent_id)
                
        list = set(agent_list)
        product_list = []
        for agent in list:
            total_commission_amount = 0
            invoices = ' '
            for agent_invoice in self:
                if  agent_invoice.agent_id.id ==  agent.id  and agent_invoice.commission_settled == False:
                    total_commission_amount = total_commission_amount + agent_invoice.commission
                    invoices = invoices +  str(agent_invoice.name) + ''\
                    
                agent_invoice.update({
                'commission_settled': True,
                })

                         
            
            invoice_line_vals = []
            invoice_line_vals = {
                     
                    'name': invoices ,
                    'account_id': 19,
                    'quantity': 1, 
                    'price_unit': total_commission_amount,
                    'account_analytic_id': 93,  
                        }
                        
            vals = {
                'partner_id': agent.id,
                'journal_id': 2,
                'invoice_date': fields.Date.today(),
                'type': 'in_invoice',
                'invoice_origin': 'Comission',
                'invoice_line_ids': [(0, 0, invoice_line_vals)],  
                }
            move = self.env['account.move'].create(vals)



        
        

    agent_id = fields.Many2one(related='partner_id.agent_id')
    comission = fields.Float(related='partner_id.comission')
    commission_rate = fields.Float(string='Commission Rate')
    commission = fields.Float(string='Commission', compute='compute_commission')
    commission_settled = fields.Boolean(string="Commission Settled", readonly=True)
    
    @api.onchange('invoice_line_ids.quantity')
    def compute_commission(self):
        for record in self:
            total_quantity = 0
            total_commission_rate = 0
            for line in record.invoice_line_ids:
                if line.package_id.shipping_grade == 'fresh':
                    total_quantity = total_quantity + (line.quantity * line.commission_rate) 
            record.commission = total_quantity
            
            
class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    
    @api.model
    def _default_get_comission(self):
        for line in self:
            return line.move_id.partner_id.comission 

    commission_rate = fields.Float(string='Commission Rate', default=_default_get_comission) 
    shiping_grade = fields.Selection(related='package_id.shipping_grade')           
