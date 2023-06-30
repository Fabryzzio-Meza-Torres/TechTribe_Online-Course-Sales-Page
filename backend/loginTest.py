import unittest
from config.qa import config
from dev.models import Clients
from dev import create_dev
from flask_sqlalchemy import SQLAlchemy
import json
import io as io


class ClientsTest(unittest.TestCase):
    def setUp(self):
        database_path = config['DATABASE_URI']
        self.dev = create_dev({'database_path': database_path})
        self.client = self.dev.test_client()

        self.new_client = {
            'firstname': 'John',
            'lastname': 'Velo',
            'email': 'john@example.com',
            'contrasena': '123mnsbbc',
        }

        self.invalid_new_client = {
            'firstname': None,
            'lastname': '21dxw2e2d',
            'email': '234ertyhj56ty',
            'contrasena': None,
        }

        response_test = self.client.post('/', json=self.new_client)
        data_test = json.loads(response_test.data)
        self.client_id_test = data_test['client']['id']

    def test_index_authenticated(self):
        # Establecer cookies para simular un usuario autenticado
        with self.dev.test_request_context('/'):
            response = self.dev.test_client().get('/')
            response.set_cookie('logged_in', 'true')
            response.set_cookie('user_id', '123')
            response.set_cookie('user_name', 'John Doe')

        # Realizar solicitud GET a la ruta /
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        # Verificar que se muestre la plantilla index.html con los datos del usuario autenticado
        self.assertIn(b'Usuario registrado', response.data)
        self.assertIn(b'123', response.data)
        self.assertIn(b'John Doe', response.data)

    def test_index_not_authenticated(self):
        # Realizar solicitud GET a la ruta /
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        # Verificar que se muestre la plantilla index.html sin datos de usuario autenticado
        self.assertNotIn(b'Usuario registrado', response.data)
        self.assertNotIn(b'user_id', response.data)
        self.assertNotIn(b'user_name', response.data)

    def test_register_success(self):
        # Realizar solicitud POST con datos válidos
        response = self.client.post('/register', data={
            'nombres': 'John',
            'apellidos': 'Doe',
            'correo': 'john.doe@gmail.com',
            'contrasena': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['message'], 'Usuario creado exitosamente')

        # Verificar que el usuario se haya creado en la base de datos
        with self.dev.app_context():
            user = Clients.query.filter_by(email='john.doe@gmail.com').first()
            self.assertIsNotNone(user)
            self.assertEqual(user.name, 'John')
            self.assertEqual(user.lastname, 'Doe')

    def test_register_missing_fields(self):
        # Realizar solicitud POST con campos faltantes
        response = self.client.post('/register', data={
            'nombres': 'John',
            'apellidos': '',
            'correo': 'john.doe@gmail.com',
            'contrasena': ''
        })
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], [
            'El campo apellidos es obligatorio',
            'Ingrese su correo electrónico',
            'El campo contrasena es obligatorio'
        ])

    def test_register_invalid_email(self):
        # Realizar solicitud POST con correo electrónico inválido
        response = self.client.post('/register', data={
            'nombres': 'John',
            'apellidos': 'Doe',
            'correo': 'john.doe@example.com',
            'contrasena': 'password123'
        })
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Ingrese un correo de Gmail válido')

    def test_register_weak_password(self):
        # Realizar solicitud POST con contraseña débil
        response = self.client.post('/register', data={
            'nombres': 'John',
            'apellidos': 'Doe',
            'correo': 'john.doe@gmail.com',
            'contrasena': '12345678'
        })
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertFalse(data['success'])
        self.assertEqual(
            data['message'], 'La contraseña no cumple con los requisitos, debe ser alfanumérica y tener al menos 8 caracteres')

    def test_register_existing_email(self):
        # Crear un usuario de prueba en la base de datos
        with self.dev.app_context():
            user = Clients(name='Jane', lastname='Smith',
                           email='jane.smith@gmail.com', password='password123')
            db.session.add(user)
            db.session.commit()
         response = self.client.post('/register', data={
            'nombres': 'John',
            'apellidos': 'Doe',
            'correo': 'jane.smith@gmail.com',
            'contrasena': 'password123'
        })
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'El correo electrónico ya ha sido registrado')


    def test_logout(self):
        # Establecer cookies para simular un usuario autenticado
        with self.dev.app.test_request_context('/'):
            response = redirect('/')
            response.set_cookie('logged_in', 'true')
            response.set_cookie('user_id', '123')
            response.set_cookie('user_name', 'John Doe')

        # Realizar solicitud GET a la ruta /logout
        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 302)

        # Verificar que las cookies se hayan eliminado correctamente
        self.assertEqual(response.headers['Location'], '/')
        self.assertNotIn('logged_in', response.headers['Set-Cookie'])
        self.assertNotIn('user_id', response.headers['Set-Cookie'])
        self.assertNotIn('user_name', response.headers['Set-Cookie'])

    if __name__ == '__main__':
    unittest.main()