# -*- coding: utf-8 -*-

from cgitb import text
from odoo import models, fields, api


class Ordenes(models.Model):
    _inherit = 'sale.order'

    notas_despacho = fields.Text(string='Notas Despacho')



class Factura(models.Model):
    _inherit = 'stock.picking'

    notas_despacho = fields.Text(string='Nota Despacho',related='sale_id.notas_despacho')

class Facturas(models.Model):
    _inherit = 'account.invoice'

    
    @api.model
    def create(self, values):
        texto=values['comment']
        texto_cortado=''
        inicio=0
        fin=60
        ciclos=int(len(texto)/fin)
        if len(texto)>fin:
            for t in range(ciclos):
                texto_cortado+=texto[inicio:fin]+'\n'
                inicio=fin
                fin+=60
        values['comment']=texto_cortado
        return super(Facturas, self).create(values)
    