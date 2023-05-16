#Imports
from flask import (
    Flask, 
    render_template, 
    request,
    jsonify,
    redirect, 
    url_for,
    flash
)
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib
import re
import json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
import os
from datetime import datetime,timedelta
import sys
#Config 
dev=Flask(__name__)
dev.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/project'
db= SQLAlchemy(dev)
migrate = Migrate(dev, db)

#Models
class Clients(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()), unique=True, nullable=False)
    firstname= db.Column(db.String(30), nullable=False)
    lastname= db.Column(db.String(50), nullable=False, unique=False)
    email= db.Column(db.String(99), nullable=False, unique=True)
    contrasena = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, server_default=db.text("now()"))

    def __init__(self, firstname, lastname, email, contrasena):
        self.firstname= firstname
        self.lastname= lastname
        self.email= email
        self.contrasena = contrasena
        self.modified_at = datetime.utcnow()
        self.created_at = datetime.utcnow()


class Trabajadores(db.Model):
    __tablename__ = 'workers'
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()), unique=True, nullable=False)
    firstname = db.Column(db.String(30), nullable=False,unique=False)
    lastname = db.Column(db.String(30), nullable=False, unique=True)
    age = db.Column(db.Integer, unique=False, nullable=False)
    especializacion= db.Column(db.String(30), nullable=False, unique=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, server_default=db.text("now()"))

    def __init__(self, firstname, lastname, age, especializacion):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.especializacion = especializacion
        self.modified_at = datetime.utcnow()
        self.created_at = datetime.utcnow()
    
class Producto(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()), unique=True, nullable=False)
    id_worker = db.Column(db.String(10), db.ForeignKey('workers.id'), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float(precision=2  ), nullable=False)
    type_product = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    duration = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, server_default=db.text("now()"))

    def ___init___(self,id_worker, name, price, type_product, description, duration):
        self.id_worker = id_worker
        self.name = name
        self.price = price 
        self.type_product = type_product
        self.description = description
        self.duration = duration
        self.modified_at = datetime.utcnow()
        self.created_at = datetime.utcnow()

class Tarjeta(db.Model):
    __tablename__ = "credit_card"
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()), unique=True, nullable=False)
    creditcard_number = db.Column(db.String(20), nullable=False)
    expiration_date= db.Column(db.Date, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    monto= db.Column(db.Float(), nullable=False)
    id_client = db.Column(db.String(10),db.ForeignKey('clients.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, server_default=db.text("now()"))

    def __init__(self, creditcard_number, password, id_client):
        self.creditcard_number = creditcard_number
        self.expiration_date = timedelta(days=30,weeks=0,months=0,year=4) # rango de 4 años y un mes desde hoy
        self.password = password
        self.id_client = id_client
        self.modified_at = datetime.utcnow()
        self.created_at = datetime.utcnow()
        

class Orden_de_Compra(db.Model):
    __tablename__ = 'purchase_order'
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()), unique=True, nullable=False)
    product_name = db.Column(db.String(50), nullable=False)
    total_price = db.Column(db.Float(), nullable=False)
    id_product = db.Column(db.String(10), db.ForeignKey('products.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, server_default=db.text("now()"))

    def __init__(self, product_name,total_price):
        self.product_name = product_name
        self.total_price = total_price
        self.modified_at = datetime.utcnow()
        self.created_at = datetime.utcnow()

# Routes
@dev.route('/', methods=['GET'])
def index():
    return render_template('index.html')




@dev.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            name = request.form.get('nombres')
            lastname = request.form.get('apellidos')
            email = request.form.get('correo')
            contrasena = request.form.get('contrasena')
            campos_validar = ['nombres', 'apellidos', 'contrasena']
            errors = []
            for campo in campos_validar:
                if not request.form.get(campo):
                    errors.append(f'El campo {campo} es obligatorio')
            
            if not email:
                errors.append('Ingrese su correo electrónico')
            elif not email.endswith('@gmail.com'):
                errors.append('Ingrese un correo de Gmail válido')
            elif not re.match(r'^(?=.*[a-zA-Z])(?=.*\d).{8,}$', contrasena):
                errors.append('La contraseña no cumple con los requisitos, debe ser alfanumérica y tener al menos 8 caracteres')
            else:
                user = Clients.query.filter_by(email=email).first()
                if user:
                    errors.append('El correo electrónico ya ha sido registrado')

            if errors:
                return jsonify({'success': False, 'message': errors}), 400
            else:
                hash_object = hashlib.sha256()
                hash_object.update(contrasena.encode('utf-8'))
                password_hash = hash_object.hexdigest()
                print(password_hash)
                new_user = Clients(name, lastname, email, password_hash)
                db.session.add(new_user)
                db.session.commit()
                return jsonify({'id': new_user.id, 'success': True, 'message': 'Usuario creado exitosamente'}), 200

        except Exception as e:
            print(e)
            print(sys.exc_info())
            db.session.rollback()
            return jsonify({'success': False, 'message': 'Error al crear usuario'}), 500

    return render_template('register.html')



@dev.route('/login', methods=['GET', 'POST'])
def login(): 
    if request.method == 'POST':
        email = request.form.get('correo')
        contrasena = request.form.get('contrasena')
        user = Clients.query.filter_by(email=email).first()
        
        if user:
            hash_object = hashlib.sha256()
            hash_object.update(contrasena.encode('utf-8'))
            password_hash = hash_object.hexdigest()
            
            if user.contrasena == password_hash:
                # Verificar la contraseña cumple con los requisitos
                if re.match(r'^(?=.*[a-zA-Z])(?=.*\d).{8,}$', contrasena):
                    return jsonify({'success': True, 'message': 'Inicio de sesión exitoso'}), 200
                else:
                    return jsonify({'success': False, 'message': 'La contraseña no cumple con los requisitos'}), 400
            else:
                return jsonify({'success': False, 'message': 'Credenciales inválidas'}), 400
        else:
            return jsonify({'success': False, 'message': 'Usuario no encontrado'}), 400
        
    else:
        return render_template('login.html')


@dev.route('/contentclient')
def resource():
    return render_template('contentclient.html')

# Run the app
if __name__ == '__main__':
    dev.run(debug=True)
else:
    print('Importing {}'.format(__name__))