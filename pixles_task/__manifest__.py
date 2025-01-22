# -*- coding: utf-8 -*-
{
    'name': "pixels task",

    'author': "Eslam Eid 01101562930",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '17.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project' , 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/project_project.xml',
        'views/hr_employee.xml',
        'reports/project_report.xml',
    ],
}
