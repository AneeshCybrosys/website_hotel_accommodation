from odoo import http
from odoo.http import request


class WebsiteForm(http.Controller):
    @http.route(['/accommodation'], type='http', auth="public", website=True)
    def accommodation(self):
        partners = request.env['res.partner'].sudo().search([])
        rooms = request.env['hotel.room'].sudo().search(
            [('available', '=', True)])

        values = {
            'partners': partners,
            'rooms': rooms
        }
        return request.render(
            "website_hotel_accommodation.online_accommodation_form", values)

    @http.route(['/accommodation/submit'], type='http', auth="public",
                website=True)
    def customer_form_submit(self, **post):
        names = request.httprequest.form.getlist('name')
        ages = request.httprequest.form.getlist('age')
        guests = []
        for name, age in zip(names,ages):
            guests.append((0, 0, {
                'name': name,
                'age': age,
            }))
        booking = request.env['hotel.accommodation'].sudo().create({
            'partner_id': int(post.get('partner_id')),
            'room_id': int(post.get('room_id')),
            'check_in_date': post.get('accommodation_date'),
            'guest_ids': guests
        })
        booking.room_id.available = False
        vals = {
            'booking': booking,
        }
        return request.render("website_hotel_accommodation.form_success", vals)
