# Imports
from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    session,
    redirect,
    url_for
)
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib
import random
import re
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_migrate import Migrate
import uuid
import traceback
from datetime import datetime, timedelta
import sys
import psycopg2
# Config
dev = Flask(__name__)

dev.config['SECRET_KEY'] = 'pass1234word'
dev.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mezatorres123@localhost:5432/project'
db = SQLAlchemy(dev)
migrate = Migrate(dev, db)

# Models


class Clients(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(
        uuid.uuid4()), unique=True, nullable=False)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(50), nullable=False, unique=False)
    email = db.Column(db.String(99), nullable=False, unique=True)
    contrasena = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True),
                            nullable=True, server_default=db.text("now()"))

    def __init__(self, firstname, lastname, email, contrasena):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.contrasena = contrasena
        self.modified_at = datetime.utcnow()
        self.created_at = datetime.utcnow()

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)


class Trabajadores(db.Model):
    __tablename__ = 'workers'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(
        uuid.uuid4()), unique=True, nullable=False)
    firstname = db.Column(db.String(30), nullable=False, unique=False)
    lastname = db.Column(db.String(30), nullable=False, unique=True)
    age = db.Column(db.Integer, unique=False, nullable=True)
    especializacion = db.Column(db.String(30), nullable=False, unique=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True),
                            nullable=True, server_default=db.text("now()"))

    def __init__(self, firstname, lastname, age, especializacion):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.especializacion = especializacion
        self.modified_at = datetime.utcnow()
        self.created_at = datetime.utcnow()


class Producto(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(
        uuid.uuid4()), unique=True, nullable=False)
    id_worker = db.Column(db.String(36), db.ForeignKey(
        'workers.id'), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    type_product = db.Column(db.String(30), nullable=False)
    duration = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True),
                            nullable=True, server_default=db.text("now()"))

    def __init__(self, id_worker, name, price, type_product, duration):
        self.id_worker = id_worker
        self.name = name
        self.price = price
        self.type_product = type_product
        self.duration = duration
        self.modified_at = datetime.utcnow()
        self.created_at = datetime.utcnow()


class Tarjeta(db.Model):
    __tablename__ = "credit_card"
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(
        uuid.uuid4()), unique=True, nullable=False)
    creditcard_number = db.Column(db.String(20), nullable=False)
    expiration_date = db.Column(db.String(36), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    monto = db.Column(db.Float(), nullable=False)
    id_client = db.Column(db.String(10), db.ForeignKey(
        'clients.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True),
                            nullable=True, server_default=db.text("now()"))

    def __init__(self, creditcard_number, expiration_date, password, id_client):
        self.creditcard_number = creditcard_number
        self.expiration_date = expiration_date
        self.password = password
        self.id_client = id_client
        self.modified_at = datetime.utcnow()
        self.created_at = datetime.utcnow()


class Orden_de_Compra(db.Model):
    __tablename__ = 'purchase_order'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(
        uuid.uuid4()), unique=True, nullable=False)
    product_name = db.Column(db.String(50), nullable=False)
    total_price = db.Column(db.Float(), nullable=False)
    id_product = db.Column(db.String(36), db.ForeignKey(
        'products.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True),
                            nullable=True, server_default=db.text("now()"))

    def __init__(self, product_name, total_price):
        self.product_name = product_name
        self.total_price = total_price
        self.modified_at = datetime.utcnow()
        self.created_at = datetime.utcnow()


class Administracion(db.Model):
    __tablename__ = 'administration'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(
        uuid.uuid4()), unique=True, nullable=False)
    id_compra = db.Column(db.String(36), db.ForeignKey(
        'purchase_order.id'), nullable=False)
    ganancia = db.Column(db.Float(), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True),
                            nullable=True, server_default=db.text("now()"))

    def __init__(self, id_compra, ganancia):
        self.id_compra = id_compra
        self.ganancia = ganancia
        self.modified_at = datetime.utcnow()
        self.created_at = datetime.utcnow()


def crear_datos_por_defecto():
    with dev.app_context():
        trabajadores = Trabajadores.query.all()
        cursos = Producto.query.all()

        if not trabajadores:
            profesor1 = Trabajadores("Marvin", "Abisrror", "25", "Python")
            profesor2 = Trabajadores("Jesus", "Bellido", "38", "Python")
            profesor3 = Trabajadores("Jose", "Fiestas", "35", "C++")
            profesor4 = Trabajadores("Ruben", "Rivas", "55", "C++")
            profesor5 = Trabajadores("Alan", "Morante", "42", "HTML/CSS")
            profesor6 = Trabajadores(
                "Jorge", "Villavicencio", "36", "HTML/CSS")
            profesor7 = Trabajadores(
                "Jose Miguel", "Renom", "55", "Matematica para CS")
            profesor8 = Trabajadores(
                "Jorge", "Tipe", "36", "Matematica para CS")
            db.session.add_all([profesor1, profesor2, profesor3,
                               profesor4, profesor5, profesor6, profesor7, profesor8])

        if not cursos:
            profesor1 = Trabajadores.query.filter_by(
                firstname="Marvin").first()
            profesor2 = Trabajadores.query.filter_by(firstname="Jesus").first()
            profesor3 = Trabajadores.query.filter_by(firstname="Jose").first()
            profesor4 = Trabajadores.query.filter_by(firstname="Ruben").first()
            profesor5 = Trabajadores.query.filter_by(firstname="Alan").first()
            profesor6 = Trabajadores.query.filter_by(firstname="Jorge").first()
            profesor7 = Trabajadores.query.filter_by(
                firstname="Jose Miguel").first()
            profesor8 = Trabajadores.query.filter_by(firstname="Jorge").first()
            curso1 = Producto(profesor1.id, "Curso Python",
                              350.00, "Curso", "6 semanas")
            asesoria1 = Producto(
                profesor2.id, "Asesoria Python", 40.00, "Asesoria", "2 horas")
            curso2 = Producto(profesor3.id, "Curso C++",
                              350.00, "Curso", "8 semanas")
            asesoria2 = Producto(profesor4.id, "Asesoria C++",
                                 40.00, "Asesoria", "2 horas")
            curso3 = Producto(profesor5.id, "HTML/CSS",
                              150.00, "Curso", "2 semanas")
            asesoria3 = Producto(
                profesor6.id, "Asesoria HTML/CSS", 40.00, "Asesoria", "2 horas")
            curso4 = Producto(profesor7.id, "Matematica para CS",
                              400.00, "Curso", "10 semanas")
            asesoria4 = Producto(
                profesor8.id, "Asesoria Matematica para CS", 40.00, "Asesoria", "2 horas")
            db.session.add_all(
                [curso1, asesoria1, curso2, asesoria2, curso3, asesoria3, curso4, asesoria4])

            db.session.commit()


crear_datos_por_defecto()

# Routes


@dev.route('/', methods=['GET'])
def index():
    logged_in = request.cookies.get('logged_in')

    if logged_in == 'true':
        user_id = request.cookies.get('user_id')
        user_name = request.cookies.get('user_name')
        data = {'message': 'Usuario registrado',
                'user_id': user_id, 'user_name': user_name}

        return render_template('index.html',  logged_in=logged_in, data=data)
    else:
        return render_template('index.html')


@dev.route('/cursos', methods=['GET'])
def showcursos():
    consulta_precio = text("SELECT price FROM products")
    resultado = db.session.execute(consulta_precio)
    precios = [row[0] for row in resultado]

    logged_in = request.cookies.get('logged_in')

    if logged_in == 'true':
        user_id = request.cookies.get('user_id')
        user_name = request.cookies.get('user_name')
        data = {'message': 'Usuario registrado',
                'user_id': user_id, 'user_name': user_name}

        return render_template('cursos.html',  logged_in=logged_in, data=data,  precios=precios)
    else:
        return render_template('cursos.html', precios=precios)


@dev.route('/asesorias', methods=['GET'])
def showasesoria():
    logged_in = request.cookies.get('logged_in')
    consulta_precio = text("SELECT price FROM products")
    resultado = db.session.execute(consulta_precio)
    precios = [row[0] for row in resultado]

    if logged_in == 'true':
        user_id = request.cookies.get('user_id')
        user_name = request.cookies.get('user_name')
        data = {'message': 'Usuario registrado',
                'user_id': user_id, 'user_name': user_name}

        return render_template('asesoria.html',  logged_in=logged_in, data=data, precios=precios)
    else:
        return render_template('asesoria.html', precios=precios)


# ----------------------------------------------------------------
@dev.route('/profesores')
def get_profesores():
    workers_results = Trabajadores.query.all()
    out = []
    for result in workers_results:
        out.append({'firstname': result.firstname,
                   'lastname': result.lastname})

    return render_template('profesores.html', workers=out)
# ----------------------------------------------------------------


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
            elif not email.endswith(('@gmail.com', '@hotmail.es', '@utec.edu.pe')):
                errors.append('Ingrese un correo de Gmail válido')
            elif not re.match(r'^(?=.*[a-zA-Z])(?=.*\d).{8,}$', contrasena):
                errors.append(
                    'La contraseña no cumple con los requisitos, debe ser alfanumérica y tener al menos 8 caracteres')
            else:
                user = Clients.query.filter_by(email=email).first()
                if user:
                    errors.append(
                        'El correo electrónico ya ha sido registrado'), 400

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
                    response = jsonify(
                        {'success': True, 'message': 'Inicio de sesión exitoso'})
                    response.set_cookie('logged_in', 'true')
                    # Agregar el ID del usuario a la cookie
                    response.set_cookie('user_id', str(user.id))
                    response.set_cookie('user_name', str(user.firstname))

                    return response, 200

                else:
                    return jsonify({'success': False, 'message': 'La contraseña no cumple con los requisitos'}), 400
            else:
                return jsonify({'success': False, 'message': 'Credenciales inválidas'}), 400
        else:
            return jsonify({'success': False, 'message': 'Usuario no encontrado'}), 400

    else:
        return render_template('login.html')


@dev.route('/logout', methods=['GET'])
def logout():
    response = redirect('/')
    response.delete_cookie('logged_in')
    response.delete_cookie('user_id')
    response.delete_cookie('user_name')
    return response


@dev.route('/orden_de_compra/<curso_name>', methods=['GET', 'POST'])
def orden_de_compra(curso_name):
    if request.method == 'GET':
        # Obtener el name del producto seleccionado
        product_name = curso_name
        product = Producto.query.filter_by(name=product_name).first()
        if product:
            product_name = product.name
            product_price = product.price
            product_type = product.type_product
        else:
            return jsonify({'success': False, 'message': 'Producto no encontrado'}), 400

        return render_template('orden.html', product_name=product_name, product_price=product_price, product_type=product_type)


@dev.route('/compra', methods=['GET', 'POST'])
def compra():
    if request.method == 'POST':
        # Obtener los datos del formulario
        creditcard_number = request.form.get('numero_tarjeta')
        expiration_date = request.form.get('fecha_vencimiento')
        password = request.form.get('contrasena')
        # Obtener el ID del cliente actualmente autenticado (puedes modificar esto según tu implementación de autenticación)
        logged_in = request.cookies.get('logged_in')
        user_id = request.cookies.get('user_id')
        monto = random.randint(300, 2000)
        # Validar los datos del formulario (puedes agregar más validaciones según tus requisitos)
        if not creditcard_number or not expiration_date or not password:
            return jsonify({'success': False, 'message': 'Todos los campos son obligatorios'}), 400

        # Crear una nueva instancia de la tarjeta
        try:
            new_tarjeta = Tarjeta(
                creditcard_number, expiration_date, password, user_id, monto)
            db.session.add(new_tarjeta)
            db.session.commit()
            return jsonify({'success': True, 'message': 'Transaccion realizada correctamente'}), 200

        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({'success': False, 'message': 'Error en la transaccion'}), 500

    return render_template('compra.html')


# Run the app
if __name__ == '__main__':
    dev.run(debug=True)
else:
    print('Importing {}'.format(__name__))
