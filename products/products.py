from flask import Blueprint, render_template, g
from .forms import Order
from .models import get_knife_by_path, get_knifes
from lang.titles import titles

products = Blueprint('products', __name__, template_folder='templates')


@products.route('/')
def index():
    knifes = get_knifes()

    return render_template('products/index.html', title='Ursus | Products', menu=g.menu, knifes=knifes)


@products.route('/order/<path>', methods=['POST', 'GET'])
def order(path):
    knife = get_knife_by_path(path)
    form = Order()

    if form.validate_on_submit():
        order_data = {
            'name': form.name.data,
            'email': form.email.data,
            'address': form.address.data,
            'payment_number': form.payment_number.data,
        }

        # Insert заявки в БД

        return render_template('products/success.html', title=titles['order_success'], menu=g.menu,
                               knife=knife,
                               form_data=order_data)

    return render_template('products/order.html', title=titles['order'], menu=g.menu, knife=knife, form=form)


@products.route('/<path>')
def show_product(path):
    knife = get_knife_by_path(path)

    return render_template('products/detail.html', title=f"{titles['show_product']} {knife.name}", menu=g.menu,
                           knife=knife)
