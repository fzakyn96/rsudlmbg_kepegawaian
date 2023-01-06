# -*- coding: utf-8 -*-
# from odoo import http


# class RsudlmbgKepegawaian(http.Controller):
#     @http.route('/rsudlmbg_kepegawaian/rsudlmbg_kepegawaian', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rsudlmbg_kepegawaian/rsudlmbg_kepegawaian/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rsudlmbg_kepegawaian.listing', {
#             'root': '/rsudlmbg_kepegawaian/rsudlmbg_kepegawaian',
#             'objects': http.request.env['rsudlmbg_kepegawaian.rsudlmbg_kepegawaian'].search([]),
#         })

#     @http.route('/rsudlmbg_kepegawaian/rsudlmbg_kepegawaian/objects/<model("rsudlmbg_kepegawaian.rsudlmbg_kepegawaian"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rsudlmbg_kepegawaian.object', {
#             'object': obj
#         })
