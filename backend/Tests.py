import unittest  # libreria de python para realizar test
from config.qa import config
from app.models import  Clients, Trabajadores, Producto, Tarjeta, Orden_de_Compra, Administracion
from app.authentication import authorize
from app import create_app
from flask_sqlalchemy import SQLAlchemy
import json
import io as io
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

    def test_showcursos(self):
        response = self.client.get('/cursos')
        data = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIn('precios', data)

    def test_showasesoria(self):
        response = self.client.get('/asesorias')
        data = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIn('precios', data)

    def test_get_profesores(self):
        response = self.client.get('/profesores')
        data = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIn('workers', data)

    def test_orden_de_compra(self):
        curso_name = 'curso1'
        response = self.client.get(f'/orden_de_compra/{curso_name}')
        data = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['product_name'], curso_name)

    def test_register_invalido(self):
        # Datos del formulario inválidos (falta el campo 'correo')
        form_data = {
            'nombres': 'John',
            'apellidos': 'Doe',
            'contrasena': 'password123'
        }

        response = self.client.post('/register', data=form_data)
        data = response.json

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Faltan campos obligatorios')

    def test_login_invalido(self):
        # Datos del formulario inválidos (contraseña incorrecta)
        form_data = {
            'correo': 'johndoe@gmail.com',
            'contrasena': 'wrongpassword'
        }

        response = self.client.post('/login', data=form_data)
        data = response.json

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Credenciales inválidas')

    def test_compra_invalido(self):
        # Datos del formulario inválidos (campo 'numero_tarjeta' demasiado corto)
        form_data = {
            'numero_tarjeta': '1234',
            'fecha_vencimiento': '12/23',
            'contrasena': 'password123'
        }

        response = self.client.post('/compra', data=form_data)
        data = response.json

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Datos de tarjeta inválidos')

    def test_pago_invalido(self):
        form_data = {
            'numero_tarjeta': '1234',
            'fecha_vencimiento': '12/23',
            'contrasena': 'password123'
        }

        response = self.client.post('/pago', json=form_data)
        data = response.json

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Datos de tarjeta inválidos')


if __name__ == '__main__':
    unittest.main()