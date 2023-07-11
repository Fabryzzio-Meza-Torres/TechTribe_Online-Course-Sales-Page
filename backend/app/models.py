#Imports
from flask_sqlalchemy import SQLAlchemy
from config.local import config
import uuid
from datetime import datetime
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
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    firstname= db.Column(db.String(30), nullable=False)
    lastname= db.Column(db.String(50), nullable=False, unique=False)
    email= db.Column(db.String(99), nullable=False, unique=True)
    contrasena = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False)
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True)
    
    def __init__(self, firstname, lastname, email,contrasena):
        self.firstname= firstname
        self.lastname= lastname
        self.email= email
        self.contrasena = contrasena
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Clients %r>' % self.email
    
    def serialize(self):  
        return {
            "id": self.id,
            "firstname": self.firstname,
            "email": self.email,
        }
    
    

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
    #workers = db.relationship('Trabajadores', backref='products', lazy=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    type_product = db.Column(db.String(30), nullable=False)
    duration = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False)
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True)

    def __init__(self, name, price, type_product, duration):
        self.name = name
        self.price = price 
        self.type_product = type_product
        self.duration = duration
        self.created_at = datetime.utcnow()
    
    def __repr__(self):
        return '<Producto %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
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
    id_client = db.Column(db.String(36), db.ForeignKey('clients.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False)
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter    
    def password(self, password):
        self.contrasena = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.contrasena, password)
    
    def verify_password(self, password):
        return check_password_hash(self.contrasena, password)

    def __init__(self, creditcard_number, expiration_date,password, id_client):
        self.creditcard_number = creditcard_number
        self.expiration_date = expiration_date
        self.password = password
        self.id_client = id_client
        self.created_at = datetime.utcnow()
    
    def __repr__(self):
        return '<Tarjeta %r>' % self.creditcard_number
    
    def serialize(self):
        return {
            "id": self.id,
            "creditcard_number": self.creditcard_number,
            "expiration_date": self.expiration_date,
            "id_client": self.id_client,
        }

class Orden_de_Compra(db.Model):
    __tablename__ = 'purchase_order'
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    status= db.Column(db.String(50), nullable=False)
    total_price = db.Column(db.Float(), nullable=False)
    id_product = db.Column(db.String(36), db.ForeignKey('products.id'), nullable=False)
    id_cliente = db.Column(db.String(36), db.ForeignKey('clients.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False)
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True)

    def __init__(self, status, total_price, id_product, id_cliente):
        self.status = status
        self.total_price = total_price
        self.id_product = id_product
        self.id_cliente = id_cliente
        self.created_at = datetime.utcnow()
    
    def __repr__(self):
        return '<Orden_de_Compra %r>' % self.id_product
    
    def serialize(self):
        return {
            "id": self.id,
            "status": self.status,
            "total_price": self.total_price,
            "id_product": self.id_product,
            "id_cliente": self.id_cliente,
        }

class Transaccion(db.Model):
    __tablename__ = 'administration'
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    id_compra = db.Column(db.String(36),db.ForeignKey('purchase_order.id'), nullable=False)
    ganancia= db.Column(db.Float(), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False)
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True)

    def __init__(self, id_compra,ganancia):
        self.id_compra = id_compra
        self.ganancia = ganancia
        self.created_at = datetime.utcnow()


def crear_datos_por_defecto(dev):
   with dev.app_context():
    trabajadores = Trabajadores.query.all()
    cursos = Producto.query.all()
    
    if not cursos:
        curso1=Producto("Python","100","Curso","3 meses")
        curso2=Producto("C++","100","Curso","3 meses")
        curso3=Producto("HTML/CSS","100","Curso","3 meses")
        curso4=Producto("Matematica para CS","100","Curso","3 meses")
        asesoria1=Producto("Python","100","Asesoria","2 horas")
        asesoria2=Producto("C++","100","Asesoria","2 horas")
        asesoria3=Producto("HTML/CSS","100","Asesoria","")
        asesoria4=Producto("Matematica para CS","100","Asesoria","1 mes")
        db.session.add_all([curso1,curso2,curso3,curso4,asesoria1,asesoria2,asesoria3,asesoria4])
    if not trabajadores:
        curso1 = Producto.query.filter(Producto.name == "Python",Producto.type_product == "Curso").first()
        curso2 = Producto.query.filter(Producto.name == "C++",Producto.type_product == "Curso").first()
        curso3 = Producto.query.filter(Producto.name == "HTML/CSS",Producto.type_product == "Curso").first()
        curso4 = Producto.query.filter(Producto.name == "Matematica para CS",Producto.type_product == "Curso").first()
        asesoria1 = Producto.query.filter(Producto.name == "Python",Producto.type_product == "Asesoria").first()
        asesoria2 = Producto.query.filter(Producto.name == "C++",Producto.type_product == "Asesoria").first()
        asesoria3 = Producto.query.filter(Producto.name == "HTML/CSS",Producto.type_product == "Asesoria").first()
        asesoria4 = Producto.query.filter(Producto.name == "Matematica para CS",Producto.type_product == "Asesoria").first()
        profesor1=Trabajadores("Marvin","Abisrror","25",curso1.id)
        profesor2=Trabajadores("Jesus","Bellido","38",asesoria1.id)
        profesor3=Trabajadores("Jose","Fiestas","35",curso2.id)
        profesor4=Trabajadores("Ruben","Rivas","55",asesoria2.id)
        profesor5=Trabajadores("Alan","Morante","42",curso3.id)
        profesor6=Trabajadores("Jorge","Villavicencio","36",asesoria3.id)
        profesor7=Trabajadores("Jose Miguel","Renom","55",curso4.id)
        profesor8=Trabajadores("Jorge","Tipe","36",asesoria4.id)
        db.session.add_all([profesor1,profesor2,profesor3,profesor4,profesor5,profesor6,profesor7,profesor8])
        db.session.commit()

