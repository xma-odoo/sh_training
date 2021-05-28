# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleWizard(models.TransientModel):
    _name = 'academy.sale.wizard'
    _description = 'Wizard: Quick Sale Orders for Session Students'
    
    # don't understand
    def _default_session(self):
        print("inside3")
        return self.env['academy.session'].browse(self._context.get('active_id'))
    
    session_id = fields.Many2one(comodel_name='academy.session',
                                string='Session',
                                required=True,
                                default=_default_session)
    # all the students currently in that session
    session_student_ids = fields.Many2many(comodel_name='res.partner',
                                string='Students in Current Session',
                                related='session_id.student_ids',
                                help='These are the students currently in the session')
    # all the students who we need to create sales order for
    # then we could filter out the existed students and know which ones we want to create the sale id for  
    student_ids = fields.Many2many(comodel_name='res.partner',
                                string='Students for Sales Order')
    
    def create_sale_orders(self):
        print("inside1")
        session_product_id = self.env['product.product'].search([('is_session_product','=',True)], limit=1)
        print("inside2")
        print("session id = ", self.session_id)
        if session_product_id:
            for student in self.student_ids:
                order_id = self.env['sale.order'].create({
                    
                    'partner_id': student.id,
                    'session_id': self.session_id,
                    'order_line':[(0, 0, {'product_id' : session_product_id.id,
                                         'price_unit': self.session_id.total_price})]
                })
    
   