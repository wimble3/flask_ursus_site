import views
from app import app
from products.products import products
from custom.custom import custom

app.register_blueprint(products, url_prefix='/products')
app.register_blueprint(custom, url_prefix='/custom')


if __name__ == '__main__':
    app.run()
