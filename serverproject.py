#Imports
from flask import (
    Flask, 
    render_template, 
    request,
    jsonify
)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
import os
from datetime import datetime,timedelta
import sys
#Config 
dev=Flask(__name__)
dev.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mezatorres1234@localhost:5432/project'
db= SQLAlchemy(dev)
migrate = Migrate(dev, db)

#Models
class Clients(db.Model):
    _tablename_ = 'clients'
    id = db.Column(db.String(10), primary_key=True, default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()") )
    firstname= db.Column(db.String(30), nullable=False)
    lastname= db.Column(db.String(50), nullable=False, unique=False)
    email= db.Column(db.String(99), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, server_default=db.text("now()"))
    
    def _init_(self, firstname, lastname, email):
        self.firstname= firstname
        self.lastname= lastname
        self.email= email
        self.modified_at = datetime.utcnow()
        self.created_at = datetime.utcnow()

class Trabajadores(db.Model):
    _tablename_ = 'workers'
    id = db.Column(db.String(10),primary_key=True, nullable=False, default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()"))
    firstname = db.Column(db.String(30), nullable=False,unique=True)
    lastname = db.Column(db.String(30), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, server_default=db.text("now()"))

    def _init_(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.modified_at = datetime.utcnow()
        self.created_at = datetime.utcnow()
    
class Producto(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.String(10),primary_key=True,nullable=False, default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()"))
    id_worker = db.Column(db.String(10), db.ForeignKey('workers.id'), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float(50.90), nullable=False)
    type_product = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    duration = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, server_default=db.text("now()"))

    def __init__(self,id_worker, name, price, type_product, description, duration):
        self.id_worker = id_worker
        self.name = name
        self.price = price 
        self.type_product = type_product
        self.description = description
        self.duration = duration
        self.modified_at = datetime.utcnow()
        self.created_at = datetime.utcnow()

class Tarjeta(db.Model):
    _tablename_ = "credit_card"
    id = db.Column(db.String(10), primary_key=True, default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()"))
    creditcard_number = db.Column(db.String(20), nullable=False)
    expiration_date= db.Column(db.Interval, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    id_client = db.Column(db.String(10),db.ForeignKey('clients.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, server_default=db.text("now()"))

    def _init_(self, creditcard_number, password, id_client):
        self.creditcard_number = creditcard_number
        self.expiration_date = timedelta(days=30,weeks=0,months=0,year=4) # rango de 4 años y un mes desde hoy
        self.password = password
        self.id_client = id_client
        self.modified_at = datetime.utcnow()
        self.created_at = datetime.utcnow()
        

class Orden_de_Compra(db.Model):
    _tablename_ = 'purchase_order'
    id= db.Column(db.String(10), primary_key=True, default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()"))
    product_name = db.Column(db.String(50), nullable=False)
    total_price = db.Column(db.Float(10000), nullable=False)
    id_product = db.Column(db.String(10), db.ForeignKey('products.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, server_default=db.text("now()"))

    def _init_(self, product_name,total_price):
        self.product_name = product_name
        self.total_price = total_price
        self.modified_at = datetime.utcnow()
        self.created_at = datetime.utcnow()

# Routes
@dev.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Run the app
if __name__ == '__main__':
    dev.run(debug=True)
else:
    print('Importing {}'.format(__name__))