from flask import render_template
from app import app
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


