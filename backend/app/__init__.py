import random
from flask import (
    Flask,
    request,
    jsonify,
    abort
)

# ,crear_datos_por_defecto
from .models import db, setup_db, Clients, Trabajadores, Producto, Tarjeta, Orden_de_Compra, Administracion
from flask_cors import CORS
import re
import hashlib
from sqlalchemy import text
from config.local import config
from .authentication import authorize

import os
import sys


def create_app(test_config=None):
    dev = Flask(__name__)
    with dev.app_context():
        setup_db(dev, test_config['database_path'] if test_config else None)
        CORS(dev, origins=['http://localhost:8080'])
#    crear_datos_por_defecto(dev)

    # Routes
# ----------------------------------------------------------GET----------------------------------------------------------------------

    @dev.route('/cursos', methods=['GET'])
    def get_cursos():
        returned_code = 200
        error_message = ''
        cursos_list = []

        try:
            search_query = request.args.get('search', None)
            if search_query:
                cursos = Producto.query.filter(
                    Producto.name.like('%{}%'.format(search_query))).all()

                cursos_list = [curso.serialize()
                               for curso in cursos]

            else:
                cursos = Producto.query.all()
                cursos_list = [curso.serialize()
                               for curso in cursos]

            if not cursos_list:
                returned_code = 404
                error_message = 'No cursos found'

        except Exception as e:

            # print(sys.exc_info())
            returned_code = 500
            error_message = 'Error retrieving cursos'

        if returned_code != 200:
            return jsonify({'success': False, 'message': error_message}), returned_code

        return jsonify({'success': True, 'cursos': cursos_list}), returned_code

    @dev.route('/asesorias', methods=['GET'])
    def get_asesorias():
        returned_code = 200
        error_message = ''
        asesorias_list = []

        try:
            search_query = request.args.get('search', None)
            if search_query:
                asesorias = Producto.query.filter(
                    Producto.name.like('%{}%'.format(search_query))).all()

                asesorias_list = [asesoria.serialize()
                                  for asesoria in asesorias]

            else:
                asesorias = Producto.query.all()
                asesorias_list = [asesoria.serialize()
                                  for asesoria in asesorias]

            if not asesorias_list:
                returned_code = 404
                error_message = 'No asesorias found'

        except Exception as e:

            # print(sys.exc_info())
            returned_code = 500
            error_message = 'Error retrieving asesorias'

        if returned_code != 200:
            return jsonify({'success': False, 'message': error_message}), returned_code

        return jsonify({'success': True, 'asesorias': asesorias_list}), returned_code

    @dev.route('/profesores', methods=['GET'])
    def get_profesores():
        returned_code = 200
        error_message = ''
        profesores_list = []

        try:
            search_query = request.args.get('search', None)
            if search_query:
                profesores = Trabajadores.query.filter(
                    Trabajadores.firstname.like('%{}%'.format(search_query))).all()

                profesores_list = [profesor.serialize()
                                   for profesor in profesores]

            else:
                profesores = Trabajadores.query.all()
                profesores_list = [profesor.serialize()
                                   for profesor in profesores]

            if not profesores_list:
                returned_code = 404
                error_message = 'No profesores found'

        except Exception as e:

            # print(sys.exc_info())
            returned_code = 500
            error_message = 'Error retrieving profesores'

        if returned_code != 200:
            return jsonify({'success': False, 'message': error_message}), returned_code

        return jsonify({'success': True, 'profesores': profesores_list}), returned_code

    @dev.route('/orden_de_compra', methods=['GET'])
    def get_orden_de_compra():
        returned_code = 200
        error_message = ''
        orden_de_compras_list = []

        try:
            search_query = request.args.get('search', None)
            if search_query:
                orden_de_compras = Orden_de_Compra.query.filter(
                    Orden_de_Compra.id_product.like('%{}%'.format(search_query))).all()

                orden_de_compras_list = [orden_de_compra.serialize()
                                         for orden_de_compra in orden_de_compras]

            else:
                orden_de_compras = Orden_de_Compra.query.all()
                orden_de_compras_list = [orden_de_compra.serialize()
                                         for orden_de_compra in orden_de_compras]

            if not orden_de_compras_list:
                returned_code = 404
                error_message = 'No orden de compra found'

        except Exception as e:

            # print(sys.exc_info())
            returned_code = 500
            error_message = 'Error retrieving orden de compra'

        if returned_code != 200:
            return jsonify({'success': False, 'message': error_message}), returned_code

        return jsonify({'success': True, 'orden_de_compras': orden_de_compras_list}), returned_code

    # ----------------------------------------------------------------POST--------------------------------------------------------------------

    @dev.route('register', methods=['POST'])
    @authorize
    def register():
        returned code = 201
        list_error = []
        try:
            body = request.json

            if 'firstname' not in body:
                list_error.append('firstname')
            else:
                name = body['name']

            if 'lastname' = not in body:
                list_error.append('lastname')
            else:
                lastname = body['lastname']

            if 'email' = not in body:
                list_error.append('email')
            else:
                email = body['email']

            if 'contrasena' = not in body:
                list_error.append('contrasena')
            else:
                contrasena = body['contrasena']

            if len(list_errors) > 0:
                returned_code = 400

            else:
                client = Clients(firstname, lastname, email, contrasena)
                db.session.add(client)
                db.session.commit()

                client_id = client.id

            except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500

            finally:
                db.session.close()

            if returned_code == 400:
                return jsonify({'success': False, 'message': 'Error register client', 'errors': list_errors}), returned_code
            elif returned_code != 201:
                abort(returned_code)
            else:
                return jsonify({'id': client_id, 'success': True, 'message': 'Client  register successfully!'}), returned_code

    @dev.route('/login', methods=['POST'])
    @authorize
    def login():
        returned_code = 201
        list_errors = []
        try:
            body = request.json

            if 'email' = not in body:
                list_errors.append('email is required')
            else:
                email = body['email']

            if 'contrasena' not in body:
                contrasena = body['contrasena']
            else:
                contrasena = body['contrasena']

            if len(list_errors) > 0
            returned_code = 400

            else:
                client = Clients.query.filter_by(email=email).first()

                if client and client.contrasena == contrasena:
                    response = jsonify(
                        {'success': True, 'message': 'Inicio de sesión exitoso'}), 200
                else:
                    return jsonify({'success': False, 'message': 'Credenciales inválidas'}),

        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500

        finally:
            db.session.close()

    @dev.route('/compra', methods=['POST'])
    @authorize
    def compra():
        returned_code = 201
        list_errors = []
        try:
            body = request.json

            if 'status' not in body:
                list_errors.append('status is required')
            else:
                status = body['status']

            if 'total_price' not in body:
                list_errors.append('total_price is required')
            else:
                total_price = body['total_price']

            if 'id_product' not in body:
                list_errors.append('id_product is required')
            else:
                id_product = body['id_product']

            if 'id_creditcard' not in body:
                list_errors.append('id_creditcard is required')
            else:
                id_creditcard = body['id_creditcard']

            if len(list_errors) > 0:
                returned_code = 400

            else:
                compra = Orden_de_Compra(
                    status_code, total_price, id_creditcard, id_product)
                db.session.add(compra)
                db.session.commit()

                compra_id = compra.id

            except Exception as e:
                print(sys.exc_info())
                db.session.rollback()
                returned_code = 500

            finally:
                db.session.close()

            if returned_code == 400:
                return jsonify({'success': False, 'message': 'Error buy product', 'errors': list_errors}), returned_code
            elif returned_code != 201:
                abort(returned_code)
            else:
                return jsonify({'id': compra_id, 'success': True, 'message': 'product successfully purchased!'}), returned_code

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

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'message': 'Method not allowed'
        }), 405

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'message': 'Resource not found'
        }), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'message': 'Internal Server error'
        }), 500

    return dev
