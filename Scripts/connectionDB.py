from flask import Flask
from flask_sqlachemy import SQLAlchemy

app = Flask(__orm__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/orm' # 'sqlite:////tmp/test.db' 
db = SQLAlchemy(app)


#Production

class Products(db.Production):
    product_id = db.Column(db.Integer, prymary_key=True)
    product_name = db.Column(db.String(50), unique=True, nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('Product.id'), nuallable=False)
    category_id = db.Column(db.Integer, unique=True, nullable=False)
    model_year = db.Column(db.String(50), unique=True, nullable=False)
    list_price = db.Column(db.String(50), unique=True, nullable=False)

#    brands = db.relationship('Brands', backref = db.backref('Products', lazy=True))

class Categories(db.Production) :
    id = db.Column(db.Integer, prymary_key=True)
    category_name = db.Column(db.String(50), unique=True, nullable=False)

def __rep__(self):
    return '<Categories %r>' % self.category_name

class Brands(db.Production):
    brand_id = db.Column(db.Integer, prymary_key=True)
    brand_name = db.Column(db.String(50), unique=True, nullable=False)

class Stocks(db.Production):
    store_id = db.Column(db.Integer, prymary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('store_id'), nullable=False)
    quantity = db.Column(db.Integer, unique=True, nullable=False)


#Sales

class Orders(db.Sales):
    order_id = db.Column(db.Integer, prymary_key=True)
    customers_id = db.Column(db.Integer, db.ForeignKey('order_id'), nullable=False)
    order_status = db.Column(db.String(50), unique=True, nullable=False)
    order_date = db.Column(db.Date, unique=True, nullable=False)
    required_date = db.Column(db.Date, unique=True, nullable=False)
    shipped_date = db.Column(db.Date, unique=True, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('order_id'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('order_id'), nullable=False)

class Customers(db.Sales):
    customers_id = db.Column(db.Integer, prymary_key=True)
    first_name = db.Column(db.String(50), unique=True, nullable=False)
    last_name = db.Column(db.String(50), unique=True, nullable=False)
    phone = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    street = db.Column(db.String(50), unique=True, nullable=False)
    city = db.Column(db.String(50), unique=True, nullable=False)
    state = db.Column(db.String(50), unique=True, nullable=False)
    zip_code = db.Column(db.Integer, unique=True, nullable=False)

class Staffs(db.Sales):
    staff_id = db.Column(db.Integer, prymary_key=True)
    first_name = db.Column(db.String(50), unique=True, nullable=False)
    last_name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    phone = db.Column(db.String(50), unique=True, nullable=False)
    active = db.Column(db.String(50), unique=True, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('staff_id'), nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('staff_id'), nullable=False)

class Stores(db.Sales):
    store_id = db.Column(db.Integer, prymary_key=True)
    store_name = db.Column(db.String(50), unique=True, nullable=False)
    phone = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    street = db.Column(db.String(50), unique=True, nullable=False)
    city = db.Column(db.String(50), unique=True, nullable=False)
    state = db.Column(db.String(50), unique=True, nullable=False)
    zip_code = db.Column(db.Integer, unique=True, nullable=False)

class Order_items(db.Sales):
    order_id = db.Column(db.Integer, prymary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('order_id'), nullable=False)
    product_id = db.Column(db.Integer, unique=True, nullable=False)
    quantity = db.Column(db.Integer, unique=True, nullable=False)
    list_price = db.Column(db.Integer, unique=True, nullable=False)
    discount = db.Column(db.Integer, unique=True, nullable=False)
