from flask import (
    request,
    jsonify
)

import sys
import jwt
from config.local import config

from functools import wraps

def authorize(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        print('authentication token: ' ,request.headers['Authorization'])
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return jsonify({
                'success': False,
                'message': 'Unauthenticated user, please provide your credentials'
            }), 401
        try:
            decoded_token=jwt.decode(token, config['SECRET_KEY'], config['ALGORITHM'])
            client_id = decoded_token.get('client_id')  # Obtener el ID del cliente del token decodificado
            kwargs['client_id'] = client_id  # Agregar el ID del cliente como argumento en kwargs
        except Exception as e:
            print('e: ', e)
            print('sys.exc_info(): ', sys.exc_info())
            return jsonify({
                'success': False,
                'message': 'Invalid Token, try a new token'
            })
        return f(*args, **kwargs)
    decorated.__name__ = f.__name__
    return decorated