# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Ordenes(models.Model):
    _inherit = 'sale.order'

    notas_despacho = fields.Text(string='Notas Despacho')



class Picking(models.Model):
    _inherit = 'stock.picking'

    notas_despacho = fields.Text(string='Nota Despacho',related='sale_id.notas_despacho')

class Factura(models.Model):
    _inherit = 'account.invoice'

    
    @api.model
    def create(self, values):
        texto=values['comment']
        texto_cortado=''
        inicio=0
        fin=60
        ciclos=int(len(texto)/fin)+1
        if len(texto)>fin:
            for t in range(ciclos):
                texto_cortado+=texto[inicio:fin]+'\n'
                inicio=fin
                fin+=60
        values['comment']=texto_cortado
        return super(Factura, self).create(values)


class Conciliacion(models.Model):
    _inherit = 'account.bank.statement.line'
    

    def process_reconciliation(self, counterpart_aml_dicts=None, payment_aml_rec=None, new_aml_dicts=None):
        conciliacion=super(Conciliacion, self).process_reconciliation()        
        payment_aml_rec.write({'statement_line_id': self.id})

        # arma la sentencia SQL
        qry = "UPDATE account_move_line SET statement_line_id = {} WHERE id ={}"

        qry=qry.format(self.id,payment_aml_rec.id)
        self.env.cr.execute(qry)        
        return payment_aml_rec

