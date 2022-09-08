from odoo import fields, models

class FilmListTag(models.Model):
    _name = "film.list.tag"
    _description = "Tags to describe films  (i.e. cult film, sequel)."

    name = fields.Char(required=True)