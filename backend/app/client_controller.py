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
            error_list.append('firstname')
        else:
            firstname = body['firstname']

        if 'lastname' not in body:
            error_list.append('lastname')
        else:
            lastname = body['lastname']

        if 'email' not in body:
            error_list.append('email')
        else:
            email = body['email']

        if 'contrasena' not in body:
            error_list.append('contrasena')
        else:
            contrasena = body['contrasena']

        client_db= Clients.query.filter_by(email=email).first()

        if client_db is not None:
            if client_db.email == email:
                error_list.append('email already exists')
        
        if len(error_list) > 0:
            returned_code = 400
        else:
            client = Clients(firstname=firstname, lastname=lastname, email=email, contrasena=contrasena)
            client_created_id= client.insert()

            token = jwt.encode({'client_id': client_created_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, config['SECRET_KEY'], config['ALGORITHM'])
    except Exception as e:
        print(e)
        abort(500) 
    if returned_code == 400:
        return jsonify({
            'success': False,
            'error': error_list,
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
    pass
