from app import application
from flask import render_template


@application.route('/')
@application.route('/index')
def index():
    user = {'nickname': 'Aashish Budania'}
    # fake posts
    posts = [
        {
            "author": "Aashish Budania",
            "subject": "Maths",
            "level": "Primary"
        },
        {
            "author": "APJ abdul",
            "subject": "Wings of fire",
            "level": "Advanced"
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
