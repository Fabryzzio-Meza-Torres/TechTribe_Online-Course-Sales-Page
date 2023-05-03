#Imports
from flask import (
    Flask, 
    render_template, 
    request,
    jsonify
)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid;
#Config 
dev=Flask(__name__)
dev.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/project'
db= SQLAlchemy(dev)

#Models
class Clients(db.Model):
    __tablename__ = 'Clients'
    id = db.Column(db.String(7), primary_key=True, default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()") )
    firstname= db.Column(db.String(30), nullable=False)
    lastname= db.Column(db.String(50), nullable=False, unique=False)
    email= db.Column(db.String(60), nullable=False, unique=True)
    foto= db.Column(db.String(500), nullable=True)
    
    def __init__(self, firstname, lastname, email, foto):
        self.firstname= firstname
        self.lastname= lastname
        self.email= email
        self.foto= foto
class Trabajadores(db.Model):
    __tablename__ = 'trabajadores'
    id = db.Column(db.String(7), nullable=False, default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()"))
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.string(50), nullable=False, unique=True)
  

class Producto(db.Model):
    __tablename__ = 'Producto'
    id = db.Column(db.String(7), nullable=False, default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()"))
    nombre = db.Column(db.String(30), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(500), nullable=False)
    foto = db.Column(db.String(500), nullable=True)
    cantidad = db.Column(db.Integer, nullable=False)
    def __init__(self, nombre, precio, descripcion, foto, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.foto = foto
        self.cantidad = cantidad

class Tarjeta(db.Model):
    __tablename__ = "tarjeta"
    numero_tarjeta = db.Column(db.String(18), nullable=False)
    fecha_vencimiento = db.Column(db.DateTime.date(2050,12,31), nullable=False)
    clave = db.Column(db.Integer(3), nullable=False)
    id_cliente = db.Column(db.Integer(8), nullable=False)
    dni = db.Column(db.Integer(8), nullable=False)
    banco_emisor = db.Column(db.String(30), nullable=False)

class Carrito(db.Model):
    __tablename__ = 'carrito'
    id_carrito = db.Column(db.String(20),nullable=False)
    nombre_producto = db.Column(db.String(30), nullable=False)
    precio_total = db.Column(db.Integer(10000), nullable=False)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
else:
    print('Importing {}'.format(__name__))

