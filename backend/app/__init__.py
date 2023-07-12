from .models import db, setup_db, Clients, Trabajadores, Producto, Tarjeta, Orden_de_Compra, Transaccion
from flask_cors import CORS

from flask import (
    Flask,
    request,
    jsonify,
    abort
)
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import ForeignKey
from flask_bcrypt import Bcrypt

import sys
import uuid
import json
from datetime import datetime


def create_app(test_config=None):
    dev = Flask(__name__)
    with dev.app_context():
        setup_db(dev, test_config['database_path'] if test_config else None)
        CORS(dev, origins=['http://localhost:8080'])
#    crear_datos_por_defecto(dev)

    # Routes 
#----------------------------------------------------------GET----------------------------------------------------------------------
    @dev.route('/productos/cursos', methods=['GET'])
    def get_cursos():
        returned_code = 200
        error_message = ''
        cursos_list = []

        try:
            search_query = request.args.get('search', None)
            if search_query:
                cursos = Producto.query.filter(
                    Producto.name.like('%{}%'.format(search_query)),
                    Producto.type_product == 'Curso'
                ).all()

                cursos_list = [curso.serialize() for curso in cursos]

            else:
                cursos = Producto.query.filter_by(type_product='Curso').all()
                cursos_list = [curso.serialize() for curso in cursos]

            if not cursos_list:
                returned_code = 404
                error_message = 'No cursos found'

        except Exception as e:
            returned_code = 500
            error_message = 'Error retrieving cursos'

        if returned_code != 200:
            return jsonify({'success': False, 'message': error_message}), returned_code

        return jsonify({'success': True, 'cursos': cursos_list}), returned_code



    @dev.route('/productos/asesorias', methods=['GET'])
    def get_asesorias():
        returned_code = 200
        error_message = ''
        asesorias_list = []

        try:
            search_query = request.args.get('search', None)
            if search_query:
                asesorias = Producto.query.filter(
                    Producto.name.like('%{}%'.format(search_query)),
                    Producto.type_product == 'Asesoria'
                ).all()

                asesorias_list = [asesoria.serialize() for asesoria in asesorias]

            else:
                asesorias = Producto.query.filter_by(type_product='Asesoria').all()
                asesorias_list = [asesoria.serialize() for asesoria in asesorias]

            if not asesorias_list:
                returned_code = 404
                error_message = 'No asesorias found'

        except Exception as e:
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

                orden_de_compras_list = [
                    orden_de_compra.serialize()for orden_de_compra in orden_de_compras]

            else:
                orden_de_compras = Orden_de_Compra.query.all()
                orden_de_compras_list = [
                    orden_de_compra.serialize()for orden_de_compra in orden_de_compras]

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

    @dev.route('/register', methods=['POST'])
    def register():
        returned_code = 201
        list_errors = []
        try:
            body = request.json

            if 'firstname' not in body:
                list_errors.append('firstname')
            else:
                firstname = body['firstname']

            if 'lastname' not in body:
                list_errors.append('lastname')
            else:
                lastname = body['lastname']

            if 'email' not in body:
                list_errors.append('email')
            else:
                email = body['email']

            if 'contrasena' not in body:
                list_errors.append('contrasena')
            else:
                contrasena = body['contrasena']

            if len(list_errors) > 0:
                returned_code = 400
            else:
                client = Clients(firstname=firstname, lastname=lastname, email=email, contrasena=contrasena)
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
            return jsonify({'success': False, 'message': 'Error registering client', 'errors': list_errors}), returned_code
        elif returned_code != 201:
            abort(returned_code)
        else:
            return jsonify({'id': client_id, 'success': True, 'message': 'Client registered successfully!'}), returned_code


    @dev.route('/login', methods=['POST'])
    def login():
        returned_code = 200
        list_errors = []

        try:
            body = request.json
            if 'email' not in body:
                list_errors.append('email is required')
            else:
                email = body['email']

            if 'contrasena' not in body:
                list_errors.append('contrasena is required')
            else:
                contrasena = body['contrasena']

                if len(list_errors) > 0:
                    returned_code = 400

                else:
                    client = Clients.query.filter_by(email=email).first()
            if len(list_errors) > 0:
                returned_code = 400
            else:
                client = Clients.query.filter_by(email=email).first()

                if client and client.check_contrasena(contrasena):
                        access_token = create_access_token(
                            identity=client.id_client)
                        returned_code = 200
                else:
                        returned_code = 401
                        list_errors.append('Cliente o contraseña incorrectos')

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
                return jsonify({'token': access_token, 'success': True, 'message': 'product successfully purchased!'}), returned_code

 
    @dev.route('/tarjeta', methods=['POST'])
    def crear_tarjeta():
        returned_code = 201
        list_errors = []

        try:
            body = request.get_json()

            if 'creditcard_number' not in body:
                list_errors.append('creditcard_number')
            else:
                creditcard_number = body['creditcard_number']

            if 'expiration_date' not in body:
                list_errors.append('expiration_date')
            else:
                expiration_date = body['expiration_date']

            if 'password' not in body:
                list_errors.append('password')
            else:
                password = body['password']

            if 'monto' not in body:
                list_errors.append('monto')
            else:
                monto = body['monto']

            if 'id_client' not in body:
                list_errors.append('id_client')
            else:
                id_client = body['id_client']

            if len(list_errors) > 0:
                returned_code = 400
            else:
                # Crear la tarjeta de crédito
                tarjeta = Tarjeta(creditcard_number=creditcard_number, expiration_date=expiration_date, password=password, monto=monto, id_client=id_client)
            
                db.session.add(tarjeta)
                db.session.commit()

                tarjeta_id = tarjeta.id

        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500


        if returned_code == 400:
            return jsonify({'success': False, 'message': 'Error creating credit card', 'errors': list_errors}), returned_code
        elif returned_code != 201:
            abort(returned_code)
        else:
            return jsonify({'id': tarjeta_id, 'success': True, 'message': 'Credit card created successfully!'}), returned_code
    
 
    
    #-------------------------------------PATCH-------------------------------------#
    #Hacemos patch, donde cuando se confirme la compra se le envia un correo al cliente, además de modificar los registros, donde se le resta el saldo al cliente y se le suma al administrador
    # ...

    @dev.route('/transacción', methods=['PATCH'])
    def confirmar_compra():
        try:
            data = request.get_json()
            #Verificar si en el json viene el id de la orden de compra
            if not data.get('orden_id'):
                return jsonify({'success': False, 'message': 'No se ha puesto el id del orden'}), 400
            else:
                orden_id = data.get('orden_id')
            
            #Obtenemos la orden de compra,y por medio de esta el cliente para obtener la tarjeta y disminuir el saldo
            orden = Orden_de_Compra.query.get(orden_id)
            cliente = Clients.query.get(orden.cliente_id)
            #Obtener el id de la tarjeta por medio del id del cliente
            tarjeta = Tarjeta.query.get(cliente.id)
            #Verificamos que el cliente tenga saldo suficiente para la compra
            if cliente.saldo < orden.total_price:
                return jsonify({'success': False, 'message': 'Saldo insuficiente'}), 400
            #Realizamos la transaccion
            tarjeta.monto += orden.total_price
            transaccion = Transaccion( orden.producto_id, orden.total_price)
            db.session.add(transaccion)
            db.session.commit()
            #Enviamos el correo al cliente
            return jsonify({'success': True, 'message': 'Compra confirmada exitosamente'}), 200

        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({'success': False, 'message': 'Error al confirmar la compra'}), 500

    
     # Error handlers

    @dev.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'message': 'Method not allowed'
        }), 405  

    @dev.errorhandler(404)
    @dev.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'message': 'Resource not found'
        }), 404
    
    @dev.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'message': 'Internal Server error'
        }), 500
    

    return dev
