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

#INFORMARIVO
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
#    crear_datos_por_defecto(dev)

    # Routes
# ----------------------------------------------------------GET----------------------------------------------------------------------
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

                asesorias_list = [asesoria.serialize()
                                  for asesoria in asesorias]

            else:
                asesorias = Producto.query.filter_by(
                    type_product='Asesoria').all()
                asesorias_list = [asesoria.serialize()
                                  for asesoria in asesorias]

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
