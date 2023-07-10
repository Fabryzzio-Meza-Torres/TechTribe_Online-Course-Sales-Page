import random
from flask import (
    Flask,
    request,
    jsonify,
    abort
)

from .models import db, setup_db, Clients, Trabajadores, Producto, Tarjeta, Orden_de_Compra, Administracion, crear_datos_por_defecto
from flask_cors import CORS
import re
import hashlib
from sqlalchemy import text
# from .users_controller import users_bp
# from .authentication import authorize

import os
import sys


def create_app(test_config=None):
    dev = Flask(__name__)
    with dev.app_context():
        # app.register_blueprint(users_bp)
        setup_db(dev, test_config['database_path'] if test_config else None)
        CORS(dev, origins='*')
    crear_datos_por_defecto(dev)

    @dev.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        response.headers.add('Access-Control-Max-Age', '10')
        return response

    # Routes
    # ----------------------------------------------------------GET----------------------------------------------------------------------
    @dev.route('/cursos', methods=['GET'])
    def showcursos():
        try:
            consulta_precio = text("SELECT price FROM products")
            resultado = db.session.execute(consulta_precio)
            precios = [row[0] for row in resultado]

            if not precios:
                returned_code = 404
                error_message = 'No prices found'
            else:
                returned_code = 200
                error_message = ''

        except Exception as e:
            returned_code = 500
            error_message = 'Error retrieving prices'

        if returned_code != 200:
            return jsonify({'success': False, 'message': error_message}), returned_code

        return jsonify({'success': True, 'precios': precios}), returned_code

    @dev.route('/asesorias', methods=['GET'])
    def showasesoria():
        try:
            consulta_precio = text("SELECT price FROM products")
            resultado = db.session.execute(consulta_precio)
            precios = [row[0] for row in resultado]

            if not precios:
                returned_code = 404
                error_message = 'No prices found'
            else:
                returned_code = 200
                error_message = ''

        except Exception as e:
            returned_code = 500
            error_message = 'Error retrieving prices'

        if returned_code != 200:
            return jsonify({'success': False, 'message': error_message}), returned_code

        return jsonify({'success': True, 'precios': precios}), returned_code

    @dev.route('/profesores', methods=['GET'])
    def get_profesores():
        try:
            workers_results = Trabajadores.query.all()
            out = [{'firstname': result.firstname, 'lastname': result.lastname}
                   for result in workers_results]

            if not out:
                returned_code = 404
                error_message = 'No workers found'
            else:
                returned_code = 200
                error_message = ''

        except Exception as e:
            returned_code = 500
            error_message = 'Error retrieving workers'

        if returned_code != 200:
            return jsonify({'success': False, 'message': error_message}), returned_code

        return jsonify({'success': True, 'workers': out}), returned_code

    @dev.route('/orden_de_compra/<curso_name>', methods=['GET'])
    def orden_de_compra(curso_name):
        try:
            # Obtener el nombre del producto seleccionado
            product_name = curso_name
            product = Producto.query.filter_by(name=product_name).first()

            if product:
                product_name = product.name
                product_price = product.price
                product_type = product.type_product

                return jsonify({'success': True, 'product_name': product_name, 'product_price': product_price, 'product_type': product_type}), 200
            else:
                return jsonify({'success': False, 'message': 'Producto no encontrado'}), 404

        except Exception as e:
            print(e)
            return jsonify({'success': False, 'message': 'Error al obtener la orden de compra'}), 500

    # ----------------------------------------------------------------POST--------------------------------------------------------------------
    @dev.route('/register', methods=['POST'])
    def register():
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
                        'El correo electrónico ya ha sido registrado')

            if errors:
                return jsonify({'success': False, 'message': errors}), 400

            hash_object = hashlib.sha256()
            hash_object.update(contrasena.encode('utf-8'))
            password_hash = hash_object.hexdigest()

            new_user = Clients(name, lastname, email, password_hash)
            db.session.add(new_user)
            db.session.commit()

            return jsonify({'id': new_user.id, 'success': True, 'message': 'Usuario creado exitosamente'}), 200

        except Exception as e:
            print(e)
            print(sys.exc_info())
            db.session.rollback()
            return jsonify({'success': False, 'message': 'Error al crear usuario'}), 500

    @dev.route('/login', methods=['POST'])
    def login():
        try:
            email = request.form.get('correo')
            contrasena = request.form.get('contrasena')
            user = Clients.query.filter_by(email=email).first()

            if user:
                hash_object = hashlib.sha256()
                hash_object.update(contrasena.encode('utf-8'))
                password_hash = hash_object.hexdigest()

                if user.contrasena == password_hash:
                    if re.match(r'^(?=.*[a-zA-Z])(?=.*\d).{8,}$', contrasena):
                        response = jsonify(
                            {'success': True, 'message': 'Inicio de sesión exitoso'})
                        response.set_cookie('logged_in', 'true')
                        response.set_cookie('user_id', str(user.id))
                        response.set_cookie('user_name', str(user.firstname))

                        return response, 200
                    else:
                        return jsonify({'success': False, 'message': 'La contraseña no cumple con los requisitos'}), 400
                else:
                    return jsonify({'success': False, 'message': 'Credenciales inválidas'}), 400
            else:
                return jsonify({'success': False, 'message': 'Usuario no encontrado'}), 400

        except Exception as e:
            print(e)
            return jsonify({'success': False, 'message': 'Error en el inicio de sesión'}), 500

    @dev.route('/compra', methods=['POST'])
    def compra():
        try:
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
            new_tarjeta = Tarjeta(
                creditcard_number, expiration_date, password, user_id, monto)
            db.session.add(new_tarjeta)
            db.session.commit()

            return jsonify({'success': True, 'message': 'Transacción realizada correctamente'}), 200

        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({'success': False, 'message': 'Error en la transacción'}), 500

    @dev.route('/pago', methods=['POST'])
    def pago():
        try:
            # Obtener los datos del formulario de pago
            data = request.get_json()
            creditcard_number = data.get('numero_tarjeta')
            expiration_date = data.get('fecha_vencimiento')
            password = data.get('contrasena')

            # Validar los datos del formulario
            if not creditcard_number or not expiration_date or not password:
                return jsonify({'success': False, 'message': 'Todos los campos son obligatorios'}), 400

            # Obtener el cliente y el administrador correspondientes
            cliente = Clients.query.get(data.get('user_id'))
            admin = Administracion.query.first()

            # Verificar que el cliente y el administrador existan
            if not cliente or not admin:
                return jsonify({'success': False, 'message': 'Error en la transacción'}), 500

            # Verificar que el cliente tenga suficiente saldo para la compra
            if cliente.saldo < admin.precio_producto:
                return jsonify({'success': False, 'message': 'Saldo insuficiente'}), 400

            # Realizar la transacción
            cliente.saldo -= admin.precio_producto
            admin.monto_total += admin.precio_producto
            db.session.commit()

            return jsonify({'success': True, 'message': 'Transacción realizada correctamente'}), 200

        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({'success': False, 'message': 'Error en la transacción'}), 500

    return dev
