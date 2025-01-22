from odoo import models, fields, api , _


class ProjectCollaborator(models.Model):
    _name = 'project.collaborator'
    _description = "Project Collaborator"

    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)
    status = fields.Selection(
        [('active', 'Active'), ('inactive', 'Inactive')],
        string="Status",
        default='inactive'
    )

    project_id = fields.Many2one('project.project', string="Project", ondelete='cascade')

    def action_set_active(self):
        self.write({'status': 'active'})

    def action_set_inactive(self):
        self.write({'status': 'inactive'})


class Employee(models.Model):
    _inherit = 'hr.employee'

    github_account = fields.Char(string="GitHub Account")
    project_collaborator_ids = fields.One2many(
        'project.collaborator', 'employee_id', string="Collaborated Projects"
    )

    def toggle_active(self):
        for record in self:
            active_projects = self.env['project.collaborator'].search([
                ('employee_id', '=', record.id),
                ('status', '=', 'active')
            ])
            if not record.active and active_projects:
                raise Warning(_(
                    "You cannot archive this employee because they are active in one or more projects."
                ))
        super(Employee, self).toggle_active()




class ProjectReport(models.AbstractModel):
    _name = 'report.pixles_task.project_report_template'
    _description = 'Project Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['project.project'].browse(docids)
        return {
            'docs': docs,
        }
