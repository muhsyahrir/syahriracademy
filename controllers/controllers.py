# -*- coding: utf-8 -*-
# from odoo import http


# class Syahrirperpus(http.Controller):
#     @http.route('/syahrirperpus/syahrirperpus/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/syahrirperpus/syahrirperpus/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('syahrirperpus.listing', {
#             'root': '/syahrirperpus/syahrirperpus',
#             'objects': http.request.env['syahrirperpus.syahrirperpus'].search([]),
#         })

#     @http.route('/syahrirperpus/syahrirperpus/objects/<model("syahrirperpus.syahrirperpus"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('syahrirperpus.object', {
#             'object': obj
#         })
