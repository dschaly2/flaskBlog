from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from datetime import date

@app.route('/')
@app.route('/index')
def index():
  user = {'username': 'Boo'}

  posts = [
    { 'author': {'username': 'John'},
      'body': 'Go Raiders!!',
      'day': date.today()},
    { 'author': {'username': 'Drew'},
      'body': 'Big win by the brownies!',
      'day': date.today() }
  ]

  return render_template('index.html', title="Home", user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('Login request for user {}, rememberMe={}'.format(form.username.data, form.rememberMe.data))
    return redirect(url_for('index'))
  return render_template('login.html', title='Sign In', form=form)
