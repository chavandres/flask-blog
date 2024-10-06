from flask import render_template
from app import app

# these are decorators to the index function
@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Andres'}
    posts = [
        {
            'author': {'username': 'John Doe'},
            'body': 'This IS a hamburger.'
        },
        {
            'author': {'username': 'Jane Doe'},
            'body': 'If you are in Costa Rica you MUST visit Tamarindo!'
        }
    ]
    return render_template('index.html',title='Home',user=user, posts=posts)