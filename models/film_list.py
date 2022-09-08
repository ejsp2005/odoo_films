# -*- coding: utf-8 -*-

from odoo import models, fields

class FilmList(models.Model):
    _name = 'film.list'
    _description = 'This is a list of films.'

    name = fields.Char(required=True)
    description = fields.Text()
    # year = fields.Char()
    # director = fields.Char()
    tags_ids = fields.Many2many("film.list.tag")
