from pyexpat import model


# -*- coding: utf-8 -*-
from odoo import models, fields, api

class FilmExpertPoints(models.Model):
    _name = 'film.expert.points'
    _description = 'Points given by Rotten Tomatoes Experts.'
    
    evaluation = fields.Char(compute='_compute_evaluation')
    points = fields.Integer()
    
    @api.depends('points')
    def _compute_evaluation(self):
        for record in self:
            if record.points > 80:
                record.evaluation = "Excellent"
            elif record.points > 60:
                record.evaluation = "Very Good"
            elif record.points > 40:
                record.evaluation = "Average"
            elif record.points > 20:
                record.evaluation = "Regular"
            else:
                record.evaluation = "Bad"

    employee_id = fields.Many2one('hr.employee', required=True)
    films_id = fields.Many2one('film.list', required=True)
