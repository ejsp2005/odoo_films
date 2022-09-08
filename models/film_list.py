# -*- coding: utf-8 -*-

from odoo import models, fields

class FilmList(models.Model):
    _name = 'film.list'
    _description = 'This is a list of films.'

    name = fields.Char(required=True, copy=False)
    description = fields.Text(copy=False)
    year = fields.Char(required=True, copy=False)
    director = fields.Char(required=True, copy=False)
    actor = fields.Char(copy=False)
    actress = fields.Char(copy=False)
    tags_ids = fields.Many2many("film.list.tag")
    gender = fields.Selection(
        selection=[
            ('scifi', 'Science Fiction'),
            ('adventure', 'Adventure'),
            ('action', 'Action'),
            ('animation', 'Animation'),
            ('war', 'War'),
            ('thriller', 'Thriller'),
            ('romance', 'Romance'),
            ('horror', 'Horror'),
            ('comedy', 'Comedy')
        ]
    )
