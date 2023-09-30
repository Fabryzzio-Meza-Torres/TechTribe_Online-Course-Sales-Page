from .models import db, setup_db, Clients,Trabajadores, Producto, Tarjeta, Transaccion, crear_datos_por_defecto
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
#from .authentication import authorize

import datetime
import sys
import os
import uuid

#
def create_app(test_config=None):
    dev = Flask(__name__)
    with dev.app_context():
        dev.register_blueprint(clients_bp)
        setup_db(dev, test_config['database_path'] if test_config else None)
        dev.run(port=5002)
        CORS(dev, origins='*')
    
    crear_datos_por_defecto(dev, db)

    @dev.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    # Routes --------------------------------------------------------

    @dev.route('/transactions', methods=['POST'])
    def create_transaccion():
        returned_code = 201
        list_errors = []

        try:
            body = request.get_json()
            print(body)

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

            monto='100'

            id_client = '4bbc751b-8e78-43cc-8f24-3645f6c8b377'

            if len(list_errors) > 0:
                returned_code = 400
            else:
                tarjeta = Tarjeta.query.filter_by(creditcard_number=creditcard_number).first()
                if tarjeta:
                    if tarjeta.password == password:
                        if tarjeta.monto >= float(monto):
                            tarjeta.monto = tarjeta.monto - float(monto)
                            db.session.add(tarjeta)
                            db.session.commit()
                        else:
                            list_errors.append('monto insuficiente')
                            returned_code = 400
                    else:
                        list_errors.append('password incorrect')
                        returned_code = 400
                else:
                    list_errors.append('creditcard_number is not registe')
                    returned_code = 400
                
                if len(list_errors) == 0:
                    transaccion = Transaccion(pago=monto, id_tarjeta=tarjeta.id, created_at=datetime.datetime.utcnow())
                    db.session.add(transaccion)
                    db.session.commit()

        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500

        if returned_code == 400:
            return jsonify({'success': False, 'message': 'Error processing transaction', 'errors': list_errors}), 400
        elif returned_code != 201:
            abort(returned_code)
        else:
            return jsonify({'success': True, 'message': 'transaction completed successfully!'}), returned_code
    



    # ERROR HANDLERS -----------------------------

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
