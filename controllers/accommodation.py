from odoo import http
from odoo.http import request


class WebsiteForm(http.Controller):
    @http.route(['/accommodation'], type='http', auth="user", website=True)
    def accommodation(self):
        partners = request.env['res.partner'].sudo().search([])
        rooms = http.request.env['hotel.room'].search([('available', '=', True)])
        # rooms = request.env['hotel.room'].sudo().search([('available', '=', True)])
        values = {}
        values.update({
            'partners': partners,
            'rooms': rooms
        })
        return request.render("website_hotel_accommodation.online_accommodation_form", values)

    @http.route(['/accommodation/submit'], type='http', auth="public",
                website=True)
    def customer_form_submit(self, **post):
        print(self.partners)
