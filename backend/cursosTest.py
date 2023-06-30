import unittest
from config.qa import config
from dev.models import Producto
from dev import create_dev
from flask_sqlalchemy import SQLAlchemy

class TestCursosRoute(unittest.TestCase):
    def setUp(self):
        database_path = config['DATABASE_URI']
        self.dev = create_dev({'database_path': database_path})
        self.cursos = self.dev.test_cursos()

    def tearDown(self):
        with self.dev.app.app_context():
            self.db.session.remove()
            self.db.drop_all()

    def test_showcursos_logged_in(self):
        # Configurar el estado de inicio de sesión para la prueba
        with self.dev.app.test_request_context('/cursos', cookies={'logged_in': 'true', 'user_id': '1', 'user_name': 'John'}):
            response = self.client.get('/cursos')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Usuario registrado', response.data)
            self.assertIn(b'user_id', response.data)
            self.assertIn(b'user_name', response.data)
            # Agrega más aserciones según sea necesario para verificar el contenido de la plantilla y otros elementos

    def test_showcursos_not_logged_in(self):
        # Configurar el estado de no inicio de sesión para la prueba
        with self.dev.app.test_request_context('/cursos'):
            response = self.client.get('/cursos')
            self.assertEqual(response.status_code, 200)
            self.assertNotIn(b'Usuario registrado', response.data)
            self.assertNotIn(b'user_id', response.data)
            self.assertNotIn(b'user_name', response.data)
            # Agrega más aserciones según sea necesario para verificar el contenido de la plantilla y otros elementos




    def test_showasesoria_logged_in(self):
        # Configurar el estado de inicio de sesión para la prueba
        with self.dev.app.test_request_context('/asesorias', cookies={'logged_in': 'true', 'user_id': '1', 'user_name': 'John'}):
            response = self.client.get('/asesorias')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Usuario registrado', response.data)
            self.assertIn(b'user_id', response.data)
            self.assertIn(b'user_name', response.data)
            # Agrega más aserciones según sea necesario para verificar el contenido de la plantilla y otros elementos

    def test_showasesoria_not_logged_in(self):
        # Configurar el estado de no inicio de sesión para la prueba
        with self.dev.app.test_request_context('/asesorias'):
            response = self.client.get('/asesorias')
            self.assertEqual(response.status_code, 200)
            self.assertNotIn(b'Usuario registrado', response.data)
            self.assertNotIn(b'user_id', response.data)
            self.assertNotIn(b'user_name', response.data)
            # Agrega más aserciones según sea necesario para verificar el contenido de la plantilla y otros elementos