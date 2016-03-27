{
    'name' : 'Custom mail wall',
    'version' : '1.0.0',
    'author' : 'IT-Projects LLC, Ivan Yelizariev',
    'license': 'LGPL-3',
    'category' : 'Custom',
    'website' : 'https://yelizariev.github.io',
    'depends' : ['gamification',
                 'gamification_extra',
                 'hr',
                 'sale',
                 'sales_team',
                 'crm',
                 'calendar',
                 'project',
                 'mail_wall_widgets',
                 'sale_mediation_custom',
                 'access_custom',
             ],
    'data':[
        'views.xml',
        'data.xml',
        ],
    'installable': False,
}
