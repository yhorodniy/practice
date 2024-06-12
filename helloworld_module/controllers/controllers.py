from odoo import http

class HelloWorldController(http.Controller):

    @http.route('/', auth='public', website=True)
    def hello_world_site(self, **kwargs):
        hello_world_record = http.request.env['ir.ui.view'].search([('key', '=', 'helloworld_module.helloworld_homepage_view')])
        if not hello_world_record:
            print("No records found")
        print(f"Record found: {hello_world_record.name}")
        # return hello_world_record.arch