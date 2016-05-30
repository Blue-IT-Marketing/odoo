{
    'name': 'Online Jobs',
    'category': 'Human Resources',
    'version': '1.0',
    'summary': 'Job Descriptions And Application Forms',
    'description': """
Odoo Contact Form
====================

        """,
    'depends': ['website_partner', 'hr_recruitment', 'website_mail', 'website_form'],
    'data': [
        'security/ir.model.access.csv',
        'security/website_hr_recruitment_security.xml',
        'data/config_data.xml',
        'views/hr_job_views.xml',
        'views/website_hr_recruitment_templates.xml',
        'views/hr_recruitment_views.xml',
    ],
    'demo': [
        'data/hr_job_demo.xml',
    ],
    'installable': True,
}
