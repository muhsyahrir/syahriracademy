# -*- coding: utf-8 -*-
{
    'name': "syahriracademy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Muh Syahrir",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizzard/studentcount_wizzard_view.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/departement_view.xml',
        'views/student_view.xml',
        'views/course_view.xml',
        'views/teacher_view.xml',
        'report/reportacademy.xml',
        'report/print_faktur_Exam.xml',
        'report/print_faktur_student.xml',
        'report/print_faktur_transaksisource.xml',
        'views/exam_view.xml',
        'views/transaksisource_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
