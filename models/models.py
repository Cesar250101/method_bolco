# -*- coding: utf-8 -*-
from ast import Continue
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
        try:
            largo=len(texto)
        except:
            largo=0
            pass
        if largo>0:
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
        conciliacion=super(Conciliacion, self).process_reconciliation(counterpart_aml_dicts, payment_aml_rec, new_aml_dicts)        
        payment_aml_rec.write({'statement_line_id': self.id})
        if payment_aml_rec:
            for p in payment_aml_rec:
                # arma la sentencia SQL
                qry = "UPDATE account_move_line SET statement_line_id = {} WHERE id ={}"

                qry=qry.format(self.id,p.id)
                self.env.cr.execute(qry)        
            return payment_aml_rec

    @api.multi
    def button_cancel_reconciliation(self):
        conciliacion=super(Conciliacion, self).button_cancel_reconciliation()        
        qry = "UPDATE account_move_line SET statement_line_id = null WHERE id ={}"

        qry=qry.format(self.journal_entry_ids.id)
        self.env.cr.execute(qry)        
        return True

