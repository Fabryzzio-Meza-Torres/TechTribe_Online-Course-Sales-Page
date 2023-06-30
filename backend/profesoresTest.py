import unittest
from config.qa import config
from dev.models import Trabajadores
from dev import create_dev
from flask_sqlalchemy import SQLAlchemy
import json
import io as io


class TestProfesoresRoute(unittest.TestCase):
    def setUp(self):
        database_path = config['DATABASE_URI']
        self.dev = create_dev({'database_path': database_path})
        self.profesores = self.dev.test_profesores()

    def tearDown(self):
        with self.dev.app.app_context():
            self.db.session.remove()
            self.db.drop_all()

    def test_get_profesores(self):
        # Agregar datos de prueba a la base de datos
        with self.dev.app.app_context():
            self.db.session.add(Trabajadores(firstname='John', lastname='Doe'))
            self.db.session.add(Trabajadores(
                firstname='Jane', lastname='Smith'))
            self.db.session.commit()

        # Realizar solicitud a la ruta /profesores
        response = self.client.get('/profesores')
        self.assertEqual(response.status_code, 200)

        # Verificar el contenido de la plantilla
        self.assertIn(b'John', response.data)
        self.assertIn(b'Doe', response.data)
        self.assertIn(b'Jane', response.data)
        self.assertIn(b'Smith', response.data)
        # Agrega más aserciones según sea necesario para verificar el contenido de la plantilla y otros elementos
