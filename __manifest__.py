{
    'name':'Digizilla',
    'version': '1.0.0',
    'author': 'Mahmoud Haney Saeed',
    'summary': "Assessment for Python Developer",
    'sequence': 1,
    'description':"This is an assignment for Python Developer role at Digizilla Company",
    'category':'Customization',
    'website':'https://github.com/mahmoudhaney',
    'depends':['base', 'mail'],
    'data': [
        "security\ir.model.access.csv",
        "views\digizilla_view.xml",
        'report\pdf_tempelate.xml',
        'report\digizilla_report.xml',
    ],
    'qweb': [
        'views\digizilla_view.xml', 
    ],
    'js': [
        'static/src/js/digizilla_hide_create_button.js',
    ],
}