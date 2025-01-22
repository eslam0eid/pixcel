from odoo import http
from odoo.http import request
import json


class EmployeeAPIController(http.Controller):
    @http.route('/api/employees/projects', type='json', auth='public', methods=['GET'], csrf=False)
    def get_employees_with_projects(self):
        try:
            # Fetch all employees
            employees = request.env['hr.employee'].sudo().search([])

            # Prepare the response data
            employee_data = []
            for employee in employees:
                # Get active projects for the employee
                active_projects = employee.project_collaborator_ids.filtered(
                    lambda c: c.status == 'active'
                ).mapped('project_id.name')

                # Add employee details to the response
                employee_data.append({
                    'employee_name': employee.name,
                    'active_projects': active_projects
                })

            # Return the JSON response
            response_data = {
                'status': 'success',
                'data': employee_data,
            }
            return request.make_response(
                json.dumps(response_data),
                headers=[('Content-Type', 'application/json')]
            )
        except Exception as e:
            # Handle errors gracefully
            error_response = {
                'status': 'error',
                'message': str(e),
            }
            return request.make_response(
                json.dumps(error_response),
                headers=[('Content-Type', 'application/json')]
            )
