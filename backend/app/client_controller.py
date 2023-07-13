from flask import (
    Blueprint,
    request,
    jsonify,
    abort,
    Response
)

import jwt
import datetime

from .models import Clients
from config.local import config

clients_bp = Blueprint('/clients', __name__)

@clients_bp.route('/clients', methods=['POST'])
def create_client():
    error_list=[]
    returned_code= 201
    try:
        body = request.get_json()

        if 'firstname' not in body:
            error_list.append('firstname is required')
        else:
            firstname = body.get('firstname')

        if 'lastname' not in body:
            error_list.append('lastname is required')
        else:
            lastname = body.get('lastname')

        if 'email' not in body:
            error_list.append('email is required')
        else:
            email = body.get('email')

        if 'password' not in body:
            error_list.append('password is required')
        else:
            password = body.get('password')

        client_db= Clients.query.filter_by(email=email).first()

        if client_db is not None:
            if client_db.email == email:
                error_list.append('email already exists')
        else:
            if len(password) < 8:
                error_list.append('Password must have at least 8 characters')
        
        if len(error_list) > 0:
            returned_code = 400
        else:
            client = Clients(firstname=firstname, lastname=lastname, email=email, password=password)
            client_created_id= client.insert()

            token = jwt.encode({'client_id': client_created_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, config['SECRET_KEY'], config['ALGORITHM'])
    except Exception as e:
        print('e: ', e)
        returned_code = 500

    if returned_code == 400:
        return jsonify({
            'success': False,
            'errors': error_list,
            'message': 'Error creating a new user'
        })
    elif returned_code != 201:
        abort(returned_code)
    else:
        return jsonify({
            'success': True,
            'token': token,
            'client_created_id': client_created_id,
        }), returned_code
    
@clients_bp.route('/api/signin', methods=['POST'])
def signin():
    error_list=[]
    returned_code= 201
    try:
        body = request.get_json()

        if 'email' not in body:
            error_list.append('email is required')
        else:
            email = body.get('email')

        if 'password' not in body:
            error_list.append('password is required')
        else:
            password = body.get('password')

        client_db= Clients.query.filter_by(email=email).first()

        if client_db is None:
            error_list.append('email does not exist')
        else:
            if client_db.password != password:
                error_list.append('password is incorrect')
        
        if len(error_list) > 0:
            returned_code = 400
        else:
            token = jwt.encode({'client_id': client_db.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, config['SECRET_KEY'], config['ALGORITHM'])
    except Exception as e:
        print('e: ', e)
        returned_code = 500

    if returned_code == 400:
        return jsonify({
            'success': False,
            'errors': error_list,
            'message': 'Error signing in'
        })
    elif returned_code != 201:
        abort(returned_code)
    else:
        return jsonify({
            'success': True,
            'token': token,
            'client_id': client_db.id,
        }), returned_code
