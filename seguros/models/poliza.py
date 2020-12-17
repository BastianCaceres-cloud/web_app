from odoo import models, fields, api

      #Modelo de las categorias de productos

class Categorias(models.Model):
    _name = 'seguros.categorias'
    name = fields.Char(string="Nombre", required=True)
    poliza_ids = fields.One2many(
        'seguros.poliza',
        'categorias_id',
        string = 'Productos')

    total_productos = fields.Integer(string = "Total Productos", compute =  "_total_productos")

    
    @api.one
    def _total_productos(self):
        self.total_productos = len(self.poliza_ids)


       #Modelo de los productos

class Poliza(models.Model):
    _name = 'seguros.poliza'

    name = fields.Char(string="Nombre", required=True)
    duration = fields.Integer(string="Cantidad", required=True)
    price = fields.Monetary('Precio', 'currency_id')
    currency_id = fields.Many2one('res.currency')
    date_contract = fields.Date(string = "Fecha de llegada")
    active = fields.Boolean('Disponibilidad', default=True)

    categorias_id = fields.Many2one('seguros.categorias', string="Categoría")
    