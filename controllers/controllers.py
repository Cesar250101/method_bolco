# -*- coding: utf-8 -*-
from odoo import http

# class MethodBolco(http.Controller):
#     @http.route('/method_bolco/method_bolco/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_bolco/method_bolco/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_bolco.listing', {
#             'root': '/method_bolco/method_bolco',
#             'objects': http.request.env['method_bolco.method_bolco'].search([]),
#         })

#     @http.route('/method_bolco/method_bolco/objects/<model("method_bolco.method_bolco"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_bolco.object', {
#             'object': obj
#         })