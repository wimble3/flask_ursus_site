from flask import Blueprint, render_template, g

custom = Blueprint('custom', __name__, template_folder='templates')


@custom.route('/')
def index():
    return render_template(
        'custom/index.html',
        menu=g.menu
    )
