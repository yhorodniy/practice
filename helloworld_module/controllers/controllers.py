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
        
        json_clients_list_path = os.path.join(module_path, '../static/src/data/mainpage_carousel.json')
        json_contact_us_bgs = os.path.join(module_path, '../static/src/data/contact_us_bgs.json')

        with open(json_clients_list_path, 'r', encoding='utf-8') as f:
            clients_list = json.load(f)

        with open(json_contact_us_bgs, 'r', encoding='utf-8') as f:
            contact_us_bgs = json.load(f)
        

        return http.request.render('helloworld_module.hw_y_h_homepage', {
            'clients_list': clients_list,
            'contact_us_bg': contact_us_bgs[0]['mainpage']
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

    @http.route('/about-us', auth='public', website=True)
    def aboutus_controller(self):
        module_path = os.path.dirname(os.path.abspath(__file__))
            
        return http.request.render('helloworld_module.hw_y_h_aboutus_page')

    
    # Requests

    @http.route('/create-contact-lead', type='http', auth='public', website=True, csrf=True)
    def create_lead(self, **kwargs):
        referer_url = request.httprequest.referrer
        sales_team = request.env['crm.team'].sudo().search([('name', '=', 'Pre-Sales')], limit=1)

        name = kwargs.get('name')
        phone = kwargs.get('phone')
        email_from = kwargs.get('email_from')
        description = kwargs.get('description')

        # Create a new lead
        if name and phone and email_from and description:
            request.env['crm.lead'].sudo().create({
                'name': name,
                'contact_name': name,
                'phone': phone,
                'mobile': phone,
                'email_from': email_from,
                'description': description,
                'priority': '3',
                'website': referer_url,
                'team_id': sales_team.id,
            })
        
        return request.redirect('/')






    # @http.route('/', type='http', auth="public", website=True)
    # def get_jobs(self):
    #     jobs = request.env['hr.job'].search([])
    #     projects = request.env['project.project'].search([])

    #     jobs_list = [ { 'id': job.id, 'name': job.name } for job in jobs ]
    #     projects_list = [ { 'id': project.id, 'name': project.name} for project in projects ]

    #     return Response(json.dumps({
    #         'jobs': jobs_list,
    #         'projects': projects_list
    #     }))

    # @http.route('/<string:name>/', auth="public", website=True)
    # def teacher(self, name):
    #     return '<h1>{}</h1>'.format(name)

    # @http.route('/<model("hr.job"):job>/', auth="public", website=True)
    # def teacher(self, job):
    #     return request.render('helloworld_module.details_view', {
    #         'vacancy': job,
    #     })

    # @http.route('/accademy/<int:id>/', auth='public', website=True)
    # def teacher_id(self, id):
    #     return '<h1>{} ({})</h1>'.format(id, type(id).__name__)
    

    # @http.route('/submit/applicant/<string:model_name>', type='http', auth="public", website=True)
    # def submit_applicant(self, model_name, **post):
    #     job_id = post.get('job_id')
    #     applicant_vals = {
    #         'name': post.get('name'),
    #         'email_from': post.get('email_from'),
    #         'partner_phone': post.get('partner_phone'),
    #         'job_id': int(job_id) if job_id else False,
    #     }
    #     applicant = request.env[model_name].sudo().create(applicant_vals)

    #     current_vacancy = request.env[model_name].sudo().search([ 'job_id' == job_id])

    #     all_applicants = request.env[model_name].sudo().search([])
    #     applicants_list = [{
    #         'id': applicant.id, 'name': applicant.name, 'email': applicant.email_from, 'phone': applicant.partner_phone
    #     } for applicant in all_applicants]
    #     # return Response(json.dumps(current_vacancy), content_type='application/json;charset=utf-8')
    #     return 'Applicant added'


    # @http.route('/submit/partner/<string:model_name>', type='http', auth='public', website=True)
    # def submit_partner(self, model_name, **post):
    #     partner_vals = {
    #         'name': post.get('name'),
    #         'email': post.get('email'),
    #         'phone': post.get('phone'),
    #         'company_id': request.env.user.company_id.id,
    #     }
        
    #     partner = request.env[model_name].sudo().create(partner_vals)
    #     all_partners = request.env[model_name].sudo().search([])
    #     partners_list = [{
    #         'id': partner.id, 'name': partner.name, 'email': partner.email, 'phone': partner.phone
    #     } for partner in all_partners]
        
    #     return Response(json.dumps(partners_list), content_type='application/json;charset=utf-8')

    
    # @http.route('/submit/ticket/<string:model_name>', type='http', auth='public', website=True)
    # def submit_ticket(self, model_name, **post):
    #     partner_vals = {
    #         'name': post.get('name'),
    #         'description': post.get('description'),
    #         'email': post.get('email'),
    #         'company_id': request.env.user.company_id.id,
    #     }
        
    #     request.env[model_name].sudo().create(partner_vals)
    #     all_tickets = request.env[model_name].sudo().search([])
    #     tickets_list = [{'id': ticket.id, 'name': ticket.name} for ticket in all_tickets]
        
    #     return Response(json.dumps(tickets_list), content_type='application/json;charset=utf-8')

    
    # @http.route('/submit/lead/<string:model_name>', type='http', auth='public', website=True)
    # def submit_lead(self, model_name, **post):
    #     lead_vals = {
    #         'name': post.get('name'),
    #         'contact_name': post.get('contact_name'),
    #         'email_from': post.get('email_from'),
    #         'phone': post.get('phone'),
    #         'company_id': request.env.user.company_id.id,
    #     }
        
    #     lead = request.env[model_name].sudo().create(lead_vals)
    #     all_leads = request.env[model_name].sudo().search([])
    #     leads_list = [{
    #         'id': lead.id, 'name': lead.name, 'contact_name': lead.contact_name, 'email': lead.email_from, 'phone': lead.phone
    #     } for lead in all_leads]
        
    #     return Response(json.dumps(leads_list), content_type='application/json;charset=utf-8')


    # @http.route('/submit/project/<string:model_name>', type='http', auth='public', website=True)
    # def submit_project(self, model_name, **post):
    #     project_vals = {
    #         'name': post.get('name'),
    #         'project_id': post.get('project_id'),
    #         'description': post.get('description'),
    #     }
        
    #     lead = request.env[model_name].sudo().create(project_vals)
    #     all_projects = request.env[model_name].sudo().search([])
    #     projects_list = [{
    #         'id': lead.id, 'name': lead.name, 'project_id': lead.project_id, 'description': lead.description
    #     } for project in all_projects]
        
    #     return Response(json.dumps(projects_list), content_type='application/json;charset=utf-8')