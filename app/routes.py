from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
           form.username.data, form.remember_me.data))
        return redirect(url_for('index'))

    return render_template('login.html', title='Login', form=form)    