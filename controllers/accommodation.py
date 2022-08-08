from odoo import http
from odoo.http import request


class WebsiteForm(http.Controller):
    @http.route(['/accommodation'], type='http', auth="user", website=True)
    def accommodation(self):
        partners = request.env['res.partner'].sudo().search([])
        rooms = request.env['hotel.room'].sudo().search([('available', '=', True)])
        values = {}
        values.update({
            'partners': partners,
            'rooms': rooms
        })
        return request.render("website_hotel_accommodation.online_accommodation_form", values)
