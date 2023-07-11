import unittest  # libreria de python para realizar test
from config.qa import config
from app.models import Clients, Trabajadores, Producto, Tarjeta, Orden_de_Compra, Administracion
#from app.authentication import authorize
from app import create_app,db
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
########################################################### GET ####################################################################    
    def test_get_cursos(self):
            response = self.client.get('/cursos')
            data = json.loads(response.data)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertTrue(data['cursos'])

    def test_get_asesorias(self):
            response = self.client.get('/asesorias')
            data = json.loads(response.data)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertTrue(data['asesorias'])

    def test_get_profesores(self):
            response = self.client.get('/profesores')
            data = json.loads(response.data)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertTrue(data['profesores'])

    def test_get_orden_de_compra(self):
            response = self.client.get('/orden_de_compra')
            data = json.loads(response.data)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertTrue(data['orden_de_compra'])

    def test_get_cursos_failed_404(self):
            response = self.client.get('/curso')
            data = json.loads(response.data)

            self.assertEqual(response.status_code, 404)
            self.assertEqual(data['success'], False)

    def test_get_asesorias_failed_404(self):
            response = self.client.get('/asesoria')
            data = json.loads(response.data)

            self.assertEqual(response.status_code, 404)
            self.assertEqual(data['success'], False)

    def test_get_profesores_failed_404(self):
            response = self.client.get('/profesor')
            data = json.loads(response.data)

            self.assertEqual(response.status_code, 404)
            self.assertEqual(data['success'], False)

    def test_get_orden_de_compra_failed_404(self):
            response = self.client.get('/orden_de_compras')
            data = json.loads(response.data)

            self.assertEqual(response.status_code, 404)
            self.assertEqual(data['success'], False)

###########################################################       ####################################################################


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

#####################################PATCH##############################################
          
if __name__ == '__main__':
    unittest.main()