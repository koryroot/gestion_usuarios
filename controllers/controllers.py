# -*- coding: utf-8 -*-
# from odoo import http


# class PruebaTecnica(http.Controller):
#     @http.route('/prueba_tecnica/prueba_tecnica/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prueba_tecnica/prueba_tecnica/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('prueba_tecnica.listing', {
#             'root': '/prueba_tecnica/prueba_tecnica',
#             'objects': http.request.env['prueba_tecnica.prueba_tecnica'].search([]),
#         })

#     @http.route('/prueba_tecnica/prueba_tecnica/objects/<model("prueba_tecnica.prueba_tecnica"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prueba_tecnica.object', {
#             'object': obj
#         })
