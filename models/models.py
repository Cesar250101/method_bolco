# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Ordenes(models.Model):
    _inherit = 'sale.order'

    notas_despacho = fields.Text(string='Notas Despacho')



class Factura(models.Model):
    _inherit = 'stock.picking'

    notas_despacho = fields.Text(string='Nota Despacho',related='sale_id.notas_despacho')
    


    
    
