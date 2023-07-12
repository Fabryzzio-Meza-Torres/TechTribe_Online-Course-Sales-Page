import unittest  # libreria de python para realizar test
from config.qa import config
from app.models import Clients, Trabajadores, Producto, Tarjeta, Orden_de_Compra, Transaccion
# from app.authentication import authorize
from app import create_app, db
from flask_sqlalchemy import SQLAlchemy
import json
import io as io
from flask import Flask
import random
import string
import datetime


def random_username(char_num):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(char_num))


class RoutesTests(unittest.TestCase):
    def setUp(self):
        database_path = config['DATABASE_URI']
        self.app = create_app({'database_path': database_path})
        self.client = self.app.test_client()


########################################################### POST  ####################################################################

        self.new_cliente = {
            'firstname': 'John',
            'lastname': 'Doe',
            'email': 'johndoe@example.com',
            'contrasena': 'password123'
        }
        self.new_product = {
            'name': 'python',
            'description': 'No me jale profe',
            'price': '100',
            'type_product': 'curso',
            'duration': '1 mes',
        }

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_register_post(self):
        response = self.client.post('/register', json={
            'firstname': 'John',
            'lastname': 'Doe',
            'email': 'johndoe@example.com',
            'contrasena': 'password123'
        })
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['success'], False)

    def test_register_400(self):
        response = self.client.post('/register', json={
            'firstname': 'John',
            'lastname': 'Doe',
            'contrasena': 'password123'
        })
        data = response.json

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Error registering client')

    def test_register_404(self):
        response = self.client.post('/registe', json={
            'firstname': 'John',
            'lastname': 'Doe',
            'contrasena': 'password123'
        })
        data = response.json

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    def test_crear_tarjeta(self):
        response = self.client.post('/register', json=self.new_cliente)
        data = json.loads(response.data)
        client_id = '24242424'
        self.new_tarjeta = {
            'id_client': client_id,
            'creditcard_number': '1234567890123456',
            'expiration_date': '12/24',
            'password': '123456',
            'monto': 1000.0
        }

        response = self.client.post('/tarjeta', json=self.new_tarjeta)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)


    def test_crear_tarjeta_400(self):
        response = self.client.post('/tarjeta', json={
            'creditcard_number': '1234567890123456',
            'expiration_date': '12/24',
            'password': '123456',
            'monto': 1000.0
        })
        data = response.json

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_crear_tarjeta_404(self):
        response = self.client.post('/register', json=self.new_cliente)
        data = json.loads(response.data)
        client_id = '23232323'
        self.new_tarjeta = {
            'id_client': client_id,
            'creditcard_number': '1234567890123456',
            'expiration_date': '12/24',
            'password': '123456',
            'monto': 1000.0
        }

        response = self.client.post('/tarjet', json=self.new_tarjeta)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], 'Resource not found')

    def test_crear_orden_de_compra_error(self):
        response = self.client.post('/compraz', json={
            'creditcard_number': '1234567890123456',
            'expiration_date': '12/24',
            'password': '123456',
            'monto': 1000.0
        })
        data = response.json

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    def test_crear_profesor_error(self):
        response = self.client.post('/profesor', json={
            'firstname': 'John',
            'lastname': 'Doe',
            'email': '',
            'contrasena': 'password123'
        })
        data = response.json
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    def test_crear_asesoria_error(self):
        response = self.client.post('/asesoria', json={
            'creditcard_number': '1234567890123456',
            'expiration_date': '12/24',
            'password': '123456',
            'monto': 1000.0
        })
        data = response.json
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    def test_crear_curso_error(self):
        response = self.client.post('/curso', json={
            'creditcard_number': '1234567890123456',
            'expiration_date': '12/24',
            'password': '123456',
            'monto': 1000.0
        })
        data = response.json
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    def test_crear_transaccion_error(self):
        response = self.client.post('/transaccion', json={
            'creditcard_number': '1234567890123456',
            'expiration_date': '12/24',
            'password': '123456',
            'monto': 1000.0
        })
        data = response.json
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')


########################################################### GET ####################################################################

    def test_get_cursos_failed_404(self):
        response = self.client.get('/curso')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)

    def test_get_asesorias_failed_404(self):
        response = self.client.get('/asesoria')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)

    def test_get_profesores_failed_404(self):
        response = self.client.get('/profesor')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)

    def test_get_orden_de_compra_failed_404(self):

        response = self.client.get('/orden_de_compras')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)

    def test_get_tarjeta_failed_404(self):
        response = self.client.get('/tarjetas')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)

    def test_get_clientes_failed_404(self):
        response = self.client.get('/clientes')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)

    def test_get_transacciones_failed_404(self):
        response = self.client.get('/transacciones')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
