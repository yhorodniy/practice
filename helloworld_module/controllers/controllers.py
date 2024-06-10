from odoo import http

class HelloWorldController(http.Controller):

    @http.route('/hello-world-record', auth='public', website=True)
    def hello_world_page(self, **kwargs):
        hello_world_record = http.request.env['helloworld.module'].search([], limit=1)
        if not hello_world_record:
            print("No records found")
        print(f"Record found: {hello_world_record}")
        print(f"Title: {hello_world_record.title}")
        return http.request.render('helloworld_module.helloworld_view', {
            'hello_world_record': hello_world_record
        })