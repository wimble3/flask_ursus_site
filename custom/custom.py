from flask import Blueprint, render_template, g, request, jsonify, flash
from .forms import EmptyForm
from .models import *

custom = Blueprint('custom', __name__, template_folder='templates', static_folder='static')


@custom.route('/', methods=['POST', 'GET'])
def index():
    form = EmptyForm()

    configurator_data = {
        'length': get_prices(LengthPrice),
        'blade_material': get_prices(BladeMaterialPrice),
        'blade_length': get_prices(BladeLengthPrice),
        'blade_thickness': get_prices(BladeThicknessPrice),
        'handle_material': get_prices(HandleMaterialPrice),
        'coating': get_prices(CoatingPrice),
    }

    if request.method == 'POST':
        if len(request.form.get('name')) > 50 or \
                len(request.form.get('email')) > 50 or \
                len(request.form.get('address')) > 50 or \
                len(request.form.get('payment_number')) > 50:
            flash('No more than 50 symbols', category='error')
        else:
            add_custom_order(
                name=request.form.get('name'),
                email=request.form.get('email'),
                address=request.form.get('address'),
                payment_number=request.form.get('payment_number'),
                length=request.form.get('length'),
                price=request.form.get('total_price'),
                blade_material=request.form.get('blade_material'),
                blade_length=request.form.get('blade_length'),
                blade_thickness=request.form.get('blade_thickness'),
                handle_material=request.form.get('handle_material'),
                coating=request.form.get('coating'),
            )
            flash('Thank you for the order!', category='success')

    return render_template('custom/index.html', menu=g.menu, configurator_data=configurator_data, form=form)


@custom.route('/ajax')
def ajax():
    length = request.args.get('length')
    blade_material = request.args.get('blade_material')
    blade_length = request.args.get('blade_length')
    blade_thickness = request.args.get('blade_thickness')
    handle_material = request.args.get('handle_material')
    coating = request.args.get('coating')

    prices = [
        int(get_price_by_value(LengthPrice, length).price),
        int(get_price_by_value(BladeLengthPrice, blade_length).price),
        int(get_price_by_value(BladeThicknessPrice, blade_thickness).price),
        int(get_price_by_value(BladeMaterialPrice, blade_material).price),
        int(get_price_by_value(HandleMaterialPrice, handle_material).price),
        int(get_price_by_value(CoatingPrice, coating).price)
    ]

    total_price = 0
    for price in prices:
        total_price += price

    return jsonify({'total_price': total_price})
