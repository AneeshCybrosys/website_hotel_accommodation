from odoo import http
from odoo.http import request


class WebsiteForm(http.Controller):
    @http.route(['/accommodation'], type='http', auth="public", website=True)
    def accommodation(self):
        partners = request.env['res.partner'].sudo().search([])
        rooms = request.env['hotel.room'].sudo().search([('available', '=', True)])
        values = {}
        values.update({
            'partners': partners,
            'rooms': rooms
        })
        return request.render("website_hotel_accommodation.online_accommodation_form", values)

    @http.route(['/accommodation/submit'], type='http', auth="public",
                website=True)
    def customer_form_submit(self, **post):
        booking = request.env['hotel.accommodation'].sudo().create({
            'partner_id': int(post.get('partner_id')),
            'room_id': int(post.get('room_id')),
            'check_in_date': post.get('accommodation_date'),
            'guest_ids': [(0, 0, {
                'name': 'figure',
            })]
        })
        # booking.room_id.available = False
        vals = {
            'booking': booking,
        }
        print(booking,'booking',"vals",vals['booking'].id)
        return request.render("website_hotel_accommodation.form_success", vals)

    @http.route(['/guests'], type='http', auth="public",
                website=True)
    def add_guests(self, **post):
        print(post,"yayaya")
