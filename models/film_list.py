# -*- coding: utf-8 -*-
from copy import copy
from wsgiref.handlers import format_date_time
from odoo import models, fields

class FilmList(models.Model):
    _name = 'film.list'
    _description = 'This is a list of films.'

    name = fields.Char(required=True)
    description = fields.Text()
    year_of_the_film = fields.Integer()
    director = fields.Char()
    
