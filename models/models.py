# -*- coding: utf-8 -*-

from odoo import models, fields, api


class persona(models.Model):
     _name = 'prueba_tecnica.persona'
     _description = 'prueba_tecnica.prueba_tecnica'

     nombre = fields.Char(required=True)#   nombre 
     cedula = fields.Char(required=True)#   Cedula // agregar api para que los datos sean validados en la cedula
     correo = fields.Char(required=True)#   correo 
     telefono = fields.Char()#   telefono #
     f_nacimiento = fields.Date(required=True)#   Fecha de nacimiento 
     direction = fields.Char()#   Direccion #
#   
