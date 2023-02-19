from flask import render_template, g
from app import app
from models import get_menu_items
from lang.titles import titles


@app.before_request
def before_request():
    g.menu = get_menu_items()


@app.route('/')
def index():
    return render_template('index.html', title=titles['index'], menu=g.menu)


@app.route('/requisites')
def requisites():
    return render_template('requisites.html', title=titles['requisites'], menu=g.menu)


@app.errorhandler(500)
@app.errorhandler(404)
@app.errorhandler(405)
def error(e):
    return render_template('error.html', title=titles['error'], menu=g.menu, error=e)
