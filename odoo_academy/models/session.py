# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Session(models.Model):
    _name = 'academy.session'
    _description = 'Session info.'
    
    date_start = fields.Date(string="Start Date")
    date_end = fields.Date(string='End Date')
    course_id = fields.Many2one(comodel_name='academy.course', 
                                string='COurse',
                                ondelete='cascade', #delted when the course is deleted
                                required=True)
    name = fields.Char(string='Title', related='course_id.name')
    
    instructor_id = fields.Many2one(comodel_name='res.partner', string='Instructor')
    
    student_ids = fields.Many2many(comodel_name='res.partner', string='Students')
    