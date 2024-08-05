from datetime import datetime
from werkzeug.exceptions import BadRequest
from odoo import http
import odoo
from odoo.http import Controller, request, Response
import json
import os

class HelloWorldController(Controller):

    # Pages
    @http.route('/', auth='public', website=True)
    def homepage_controller(self):
        module_path = os.path.dirname(os.path.abspath(__file__))
        
        json_homepage_lists = os.path.join(module_path, '../static/src/data/mainpage_page.json')

        with open(json_homepage_lists, 'r', encoding='utf-8') as f:
            homepage_lists = json.load(f)

        return http.request.render('helloworld_module.hw_y_h_homepage', {
            'processes': homepage_lists[0]['processes'],
            'integrations': homepage_lists[0]['integrations'],
            'cases': homepage_lists[0]['cases'],
            'clients_list': homepage_lists[0]['clients'],
        })

    @http.route('/about-odoo', auth='public', website=True)
    def aboutodoo_controller(self):
        module_path = os.path.dirname(os.path.abspath(__file__))
                
        json_advantages_list = os.path.join(module_path, '../static/src/data/about_odoo_page.json')

        with open(json_advantages_list, 'r', encoding='utf-8') as f:
            advantages_list = json.load(f)

        return http.request.render('helloworld_module.hw_y_h_aboutodoo_page',   {
            'advantages_list': advantages_list
        })

    @http.route('/modules', auth='public', website=True)
    def modules_controller(self):
        module_path = os.path.dirname(os.path.abspath(__file__))
                          
        json_modules_list = os.path.join(module_path, '../static/src/data/modules_page.json')

        with open(json_modules_list, 'r', encoding='utf-8') as f:
            modules_list = json.load(f)

        return http.request.render('helloworld_module.hw_y_h_modules_page', {
            'modules_list': modules_list[0],
            'cards_list': modules_list[1]
        })

    @http.route('/contacts', auth='public', website=True)
    def contacts_controller(self):
        module_path = os.path.dirname(os.path.abspath(__file__))
                          
        json_contacts_page_data = os.path.join(module_path, '../static/src/data/contacts_page.json')

        with open(json_contacts_page_data, 'r', encoding='utf-8') as f:
            contacts_page_data = json.load(f)

        return http.request.render('helloworld_module.hw_y_h_contacts', {
            'team': contacts_page_data[0]['team'],
            'services': contacts_page_data[0]['services'],
            'coop_list': contacts_page_data[0]['coop'],
            'solutions': contacts_page_data[0]['solutions'],
            'advantages': contacts_page_data[0]['advantages'],
            'obligations': contacts_page_data[0]['obligations'],
            'differences': contacts_page_data[0]['differences'],
        })

    
    # Requests

    @http.route('/form/submit/callback', type='http', auth='public', website=True, csrf=True)
    def create_lead(self, **kwargs):
        sales_team = request.env['crm.team'].sudo().search([('name', '=', 'Sales')], limit=1)
        medium_id = request.env['crm.lead'].sudo().search([('medium_id', '=', 'Form')], limit=1)
        source_id = request.env['crm.lead'].sudo().search([('medium_id', '=', 'СайтToDo')], limit=1)

        name = kwargs.get('name')
        phone = kwargs.get('phone')
        email_from = kwargs.get('email_from')
        description = kwargs.get('description')

        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        utm_source = request.params.get('utm_source')
        utm_medium = request.params.get('utm_medium')
        utm_campaign = request.params.get('utm_campaign')
        utm_term = request.params.get('utm_term')


        # Create a new lead
        if name and phone and email_from and description:
            request.env['crm.lead'].sudo().create({
                'name': f'Замовити дзвінок - {name} - {current_date}',
                'contact_name': name,
                'phone': phone,
                'email_from': email_from,
                'description': f'Коментар:\n {description}',
                'company_id': "",
                'medium_id': medium_id.id,
                'source_id': source_id.id,
                'utm_source': utm_source,
                'utm_medium': utm_medium,
                'utm_campaign': utm_campaign,
                'utm_term': utm_term,
                'team_id': sales_team.id,
                'user_id': "",
            })
        
        return request.redirect('/')