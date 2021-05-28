# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import timedelta

class Session(models.Model):
    _name = 'academy.session'
    _description = 'Session info.'
    
    date_start = fields.Date(string="Start Date",
                            default=fields.Date.today)
    
    date_end = fields.Date(string='End Date',
                          compute='_compute_end_date',
                          inverse='_inverse_end_date',
                          store=True) 
    
    duration = fields.Integer(string="Session Days",
                             default=1)
    
    course_id = fields.Many2one(comodel_name='academy.course', 
                                string='COurse',
                                ondelete='cascade', #delted when the course is deleted
                                required=True)
    name = fields.Char(string='Title', related='course_id.name')
    
    instructor_id = fields.Many2one(comodel_name='res.partner', string='Instructor')
    
    student_ids = fields.Many2many(comodel_name='res.partner', string='Students')
    
    total_price = fields.Float(string='Total Price',
                              related='course_id.total_price')
    
    @api.depends('date_start', 'duration')
    def _compute_end_date(self):
        for record in self:
            if not (record.date_start and record.duration):
                record.date_end = record.date_start
            else:
                duration = timedelta(days=record.duration)
                record.date_end = record.date_start + duration
                
    def _inverse_end_date(self):
        for record in self:
            if record.date_start and record.date_end:
                record.duration = (record.date_end - record.date_start).days + 1
            else:
                continue
                
    