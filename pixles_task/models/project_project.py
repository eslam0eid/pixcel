from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'

    odoo_version = fields.Integer(string="Odoo Version")
    odoo_type = fields.Selection(
        [('community', 'Community'), ('enterprise', 'Enterprise')],
        string="Odoo Type",
        default='enterprise'
    )
    github_repo_name = fields.Char(string="GitHub Repository Name")
    github_repo_url = fields.Char(string="GitHub Repository URL")
    hosting = fields.Selection(
        [('on_prem', 'On Prem'),
         ('cloud_hosting', 'Cloud Hosting'),
         ('odoo_sh', 'Odoo SH'),
         ('odoo_online', 'Odoo Online')],
        string="Hosting"
    )
    hosting_description = fields.Html(string="Hosting Description")

    collaborator_ids = fields.One2many('project.collaborator', 'project_id', string="Collaborators")
