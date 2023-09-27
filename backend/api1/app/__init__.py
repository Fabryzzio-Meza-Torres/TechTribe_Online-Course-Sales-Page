from .models import db, setup_db, Clients,Trabajadores, Producto, Tarjeta, Transaccion
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
from .client_controller import clients_bp
from .authentication import authorize

import sys
import os

#AUTHENTICATION
def create_app(test_config=None):
    dev = Flask(__name__)
    with dev.app_context():
        dev.register_blueprint(clients_bp)
        setup_db(dev, test_config['database_path'] if test_config else None)
        CORS(dev, origins=['http://localhost:8080'])

    @dev.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response



    @dev.route('/register', methods=['POST'])
    def register():
        returned_code = 201
        list_errors = []
        try:
            body = request.json

            print(body);

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
                client = Clients(
                    firstname=firstname, lastname=lastname, email=email, contrasena=contrasena)
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
            return jsonify({'success': False, 'message': 'Error registering client', 'errors': list_errors}),400 
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



# ERROR HANDLERS

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
