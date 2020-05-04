from app import application
from flask import render_template


@application.route('/')
@application.route('/index')
def index():
    user = {'nickname': 'Aashish Budania'}
    return render_template('index.html', title='Home', user=user)
