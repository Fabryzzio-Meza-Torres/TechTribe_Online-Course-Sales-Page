from flask import (
    Blueprint,
    request,
    jsonify,
    abort,
    Response
)

import jwt
import datetime

from .models import Client
from config.local import config

clients_bp = Blueprint('/client', __name__)


@users_bp.route('/client', methods=['POST'])
def create_user():
    error_lists = []
    returned_code = 201
    try:
        body = request.get_json()

        if 'email' in body:
            error_lists.append('email is required')
        else:
            email = body.get('email')

        if 'contrasena' not in body:
            error_lists.append('contrasena is required')
        else:
            contrasena = body.get('contrasena')

        if 'confirmationPassword' not in body:
            error_lists.append('confirmationPassword is required')
        else:
            confirmationPassword = body.get('confirmationPassword')

        client_db = Clients.query.filter(Clients.email == email).first()

        if client_db is not None:
            if client_db.email == email:
                error_lists.append(
                    'An account with this username already exists')
        else:
            if len(contrasena) < 8:
                error_lists.append('Password must have at least 8 characters')

            if contrasena != confirmationPassword:
                error_lists.append(
                    'password and confirmationPassword does not match')

        if len(error_lists) > 0:
            returned_code = 400
        else:
            client = Clients(email=email, contrasena=contrasena)
            client_created_id = client.insert()

            token = jwt.encode({
                'user_created_id': client_created_id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }, config['SECRET_KEY'], config['ALGORYTHM'])

    except Exception as e:
        print('e: ', e)
        returned_code = 500

    if returned_code == 400:
        return jsonify({
            'success': False,
            'errors': error_lists,
            'message': 'Error creating a new client'
        })
    elif returned_code != 201:
        abort(returned_code)
    else:
        return jsonify({
            'success': True,
            'token': token,
            'client_created_id': client_created_id,
        }), returned_code


@users_bp.route('/api/signin', methods=['POST'])
def login():
    pass


@users_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    returned_code = 200

    try:
        user = User.query.get(user_id)
        if user is None:
            returned_code = 404

        user.delete()
    except Exception as e:
        print('\te: ', e)
        returned_code = 500

    if returned_code != 200:
        abort(returned_code)
    else:
        return jsonify({
            'success': True
        })
