#Imports
from flask_sqlalchemy import SQLAlchemy
from config.local import config
import uuid
import random
from datetime import datetime
from sqlalchemy.orm import synonym
from werkzeug.security import generate_password_hash, check_password_hash
import sys

db= SQLAlchemy()

def setup_db(app, database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = config['DATABASE_URI'] if database_path is None else database_path
    db.app = app
    db.init_app(app)
    db.create_all()

#Models
class Clients(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(50), nullable=False, unique=False)
    email = db.Column(db.String(99), nullable=False, unique=True)
    contrasena = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False)
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True)
    @property
    def password(self):
        return self.contrasena

    @password.setter
    def password(self, password):
        self.contrasena = generate_password_hash(password)


    
    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Clients %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "email": self.email,
        }

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            client_created_id = self.id
        except Exception as e:
            print(sys.exc_info())
            print('e: ', e)
            db.session.rollback()
            raise e
        finally:
            db.session.close()

        return client_created_id    

class Trabajadores(db.Model):
    __tablename__ = 'workers'
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False, unique=False)
    age = db.Column(db.Integer, unique=False, nullable=True)
    producto_id = db.Column(db.String(36), db.ForeignKey('products.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False)
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True)

    def __init__(self, firstname, lastname, age, producto_id):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.producto_id = producto_id
        self.created_at = datetime.utcnow()
    
    def __repr__(self):
        return '<Trabajadores %r %r>' % (self.firstname, self.lastname)
    
    def serialize(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "age": self.age,
            "producto_id": self.producto_id,
        }
    
class Producto(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(350), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    type_product = db.Column(db.String(30), nullable=False)
    duration = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False)
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True)

    def __init__(self, name, price, description, type_product, duration):
        self.name = name
        self.price = price 
        self.description = description
        self.type_product = type_product
        self.duration = duration
        self.created_at = datetime.utcnow()
    
    def __repr__(self):
        return '<Producto %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "type_product": self.type_product,
            "duration": self.duration,
        }
    
class Tarjeta(db.Model):
    __tablename__ = "credit_card"
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    creditcard_number = db.Column(db.String(20), nullable=False)
    expiration_date= db.Column(db.String(36), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    monto= db.Column(db.Float(), nullable=False)
    id_client = db.Column(db.String(36), db.ForeignKey('clients.id'), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda:datetime.utcnow())
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True)
  
    def __init__(self, creditcard_number, expiration_date, password,  id_client):
        self.creditcard_number = creditcard_number
        self.expiration_date = expiration_date
        self.password = password
        #Se asigna un monto random
        self.monto = random.randint(100, 1000)
        self.id_client = id_client
        self.created_at = datetime.utcnow()

    def check_password(self, password):
        return check_password_hash(self.contrasena, password)
    
    def verify_password(self, password):
        return check_password_hash(self.contrasena, password)

    
    def __repr__(self):
        return '<Tarjeta %r>' % self.creditcard_number
    
    def serialize(self):
        return {
            "id": self.id,
            "creditcard_number": self.creditcard_number,
            "expiration_date": self.expiration_date,
            "id_client": self.id_client,
        }

class Transaccion(db.Model):
    __tablename__ = 'administration'
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    pago = db.Column(db.Float(), nullable=False)
    id_tarjeta = db.Column(db.String(36), db.ForeignKey('credit_card.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False)
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True)

    def __init__(self,ganancia):
        self.ganancia = ganancia
        self.created_at = datetime.utcnow()

