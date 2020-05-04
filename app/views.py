from app import application
from flask import render_template


@application.route('/')
@application.route('/index')
def index():
    user = {'nickname': 'Aashish Budania'}
    # fake posts
    posts = [
        {
            "author": {"nickname": "Aashish Budania"},
            "subject": "Maths",
            "level": "Primary",
            "body": "Consistency > Hard Work > Talent"
        },
        {
            "author": {"nickname": "Abdul"},
            "subject": "Wings of fire",
            "level": "Advanced",
            "body": "To shine like a sun, first you have to burn like a sun"
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
