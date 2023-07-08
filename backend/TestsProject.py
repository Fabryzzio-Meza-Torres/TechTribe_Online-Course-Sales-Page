import unittest
from config.qa import config
from dev.db import dev, test_db
from dev import create_dev
from sqlalchemy import text
import json
from flask import request, jsonify


class TestsClients(unittest.TestCase):
    def setUp(self):
        database_path = config['DATABASE_URI']
        self.dev = create_dev({'database_path': database_path})
        self.client = self.dev.test_client()

    def test_register_new_client_success(self):
        register_data = {
            'firstname': 'Josue',
            'lastname': 'Velo',
            'email': 'josue.velo@gmail.com',
            'contrasena': '76917241utec'
        }

        response = self.client.post('/register', data=register_data)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['id'])
        self.assertEqual(data['message'], 'Usuario creado exitosamente')

    def test_register_new_client_invalied_email(self):

        register_data = {
            'firstname': 'Josue',
            'lastname': 'Velo',
            'email': 'josue.velo@gmail',
            'contrasena': 'josue187'
        }

        response = self.client.post('/register', data=register_data)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'])

    def test_register_new_client_invalid_password(self):

        register_data = {
            'firstname': 'Josue',
            'lastname': 'Velo',
            'email': 'josue.velo@gmail.com',
            'contrasena': 'josue18'
        }

        response = self.client.post('/register', data=register_data)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'])

    def test_login_success(self):
        login_data = {
            'correo': 'josue.velo@gmail.com',
            'contrasena': '76917241utec'
        }

        response = self.client.post('/login', data=login_data)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'Inicio de sesión exitoso')
        self.assertTrue('logged_in' in response.headers['Set-Cookie'])
        self.assertTrue('user_id' in response.headers['Set-Cookie'])
        self.assertTrue('user_name' in response.headers['Set-Cookie'])

    def test_login_invalid_credentials(self):
        login_data = {
            'correo': 'josue.velo@gmail.com',
            'contrasena': 'incorrect_password'
        }

        response = self.client.post('/login', data=login_data)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Credenciales inválidas')

    def test_login_invalid_password_format(self):
        login_data = {
            'correo': 'josue.velo@gmail.com',
            'contrasena': 'weakpassword'
        }

        response = self.client.post('/login', data=login_data)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'], 'La contraseña no cumple con los requisitos')

    def test_login_user_not_found(self):
        login_data = {
            'correo': 'nonexistent@gmail.com',
            'contrasena': 'password'
        }

        response = self.client.post('/login', data=login_data)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Usuario no encontrado')

    def test_login_server_error(self):
        login_data = {
            'correo': 'josue.velo@gmail.com',
            'contrasena': '76917241utec'
        }

        # Simular un error en el servidor
        with unittest.mock.patch('dev.models.Clients.query') as mock_query:
            mock_query.filter_by.side_effect = Exception(
                'Error en el servidor')

            response = self.client.post('/login', data=login_data)
            data = json.loads(response.data)

            self.assertEqual(response.status_code, 500)
            self.assertEqual(data['success'], False)
            self.assertEqual(data['message'], 'Error en el inicio de sesión')


class TestProducto(unittest.TestCase):
    def setUp(self):
        database_path = config['DATABASE_URI']
        self.dev = create_dev({'database_path': database_path})
        self.product = self.dev.get_product()

    with self.dev.app.app_context():
        db.create_all()
        # Agregar productos de prueba
        product1 = Product(name='Python', price=350)
        product2 = Product(name='C++', price=350)
        product3 = Product(name='HTML/CSS', price=150)
        product4 = Product(name='Matematica para CS', price=400)
        db.session.add_all([product1, product2, product3])
        db.session.commit()

    def tearDown(self):
        # Limpiar la base de datos de prueba después de cada prueba
        with self.dev.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_showcursos_success(self):
        response = self.client.get('/cursos')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('precios' in data)
        self.assertEqual(len(data['precios']), 3)

    def test_showcursos_no_prices_found(self):
        # Eliminar todos los productos para simular que no se encuentran precios
        with self.dev.app.app_context():
            db.session.query(Product).delete()
            db.session.commit()

        response = self.client.get('/cursos')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'No prices found')

    def test_showcursos_error_retrieving_prices(self):
        # Simular un error al obtener los precios mediante una consulta inválida
        with self.dev.app.app_context():
            db.session.execute(text("DROP TABLE products"))
            db.session.commit()

        response = self.client.get('/cursos')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Error retrieving prices')

    with self.dev.app.app_context():
        db.create_all()
        # Agregar productos de prueba
        product1 = Product(name='Asesoria Python', price=40)
        product2 = Product(name='Asesoria C++', price=40)
        product3 = Product(name='Asesoria HTML/CSS', price=40)
        product4 = Product(name='Asesoria Matematica para CS', price=40)
        db.session.add_all([product1, product2, product3])
        db.session.commit()

    def tearDown(self):
        # Limpiar la base de datos de prueba después de cada prueba
        with self.dev.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_showasesoria_success(self):
        response = self.client.get('/asesorias')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('precios' in data)
        self.assertEqual(len(data['precios']), 3)

    def test_showasesoria_no_prices_found(self):
        # Eliminar todos los productos para simular que no se encuentran precios
        with self.dev.app.app_context():
            db.session.query(Product).delete()
            db.session.commit()

        response = self.client.get('/asesorias')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'No prices found')

    def test_showasesoria_error_retrieving_prices(self):
        # Simular un error al obtener los precios mediante una consulta inválida
        with self.dev.app.app_context():
            db.session.execute(text("DROP TABLE products"))
            db.session.commit()

        response = self.client.get('/asesorias')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Error retrieving prices')


class TestCompra(unittest.TestCase):
    def setUp(self):
        database_path = config['DATABASE_URI']
        self.dev = create_dev({'database_path': database_path})
        self.buy = self.dev.get_buy()

        with self.dev.app.app_context():
            db.create_all()

    def tearDown(self):
        # Limpiar la base de datos de prueba después de cada prueba
        with self.dev.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_compra_success(self):
        # Simular datos válidos del formulario
        compra_data = {
            'numero_tarjeta': '1234567890123456',
            'fecha_vencimiento': '12/23',
            'contrasena': 'password'
        }

        response = self.client.post('/compra', data=compra_data)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(
            data['message'], 'Transacción realizada correctamente')

    def test_compra_missing_fields(self):
        # Simular datos del formulario faltantes
        compra_data = {
            'numero_tarjeta': '1234567890123456',
            'contrasena': 'password'
        }

        response = self.client.post('/compra', data=compra_data)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Todos los campos son obligatorios')

    def test_compra_error(self):
        # Simular un error en la transacción
        with self.dev.app.app_context():
            # Forzar un error al agregar la tarjeta a la base de datos
            def raise_error(*args, **kwargs):
                raise Exception('Error en la transacción')

            Tarjeta.add = raise_error

            # Simular datos válidos del formulario
            compra_data = {
                'numero_tarjeta': '1234567890123456',
                'fecha_vencimiento': '12/23',
                'contrasena': 'password'
            }

            response = self.client.post('/compra', data=compra_data)
            data = json.loads(response.data)

            self.assertEqual(response.status_code, 500)
            self.assertEqual(data['success'], False)
            self.assertEqual(data['message'], 'Error en la transacción')


class TestPago(unittest.TestCase):
    def setUp(self):
        database_path = config['DATABASE_URI']
        self.dev = create_dev({'database_path': database_path})
        self.pago = self.dev.get_pago()

        # Configurar el estado inicial de la base de datos de prueba
        with self.dev.app.app_context():
            db.create_all()

            # Agregar datos de prueba
            cliente = Clients(id=1, saldo=1000)
            admin = Administracion(id=1, precio_producto=500)
            db.session.add(cliente)
            db.session.add(admin)
            db.session.commit()

    def tearDown(self):
        # Limpiar la base de datos de prueba después de cada prueba
        with self.dev.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_pago_success(self):
        # Simular datos válidos del formulario de pago
        pago_data = {
            'numero_tarjeta': '1234567890123456',
            'fecha_vencimiento': '12/23',
            'contrasena': 'password',
            'user_id': 1
        }

        response = self.client.post('/pago', json=pago_data)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(
            data['message'], 'Transacción realizada correctamente')

    def test_pago_missing_fields(self):
        # Simular datos del formulario de pago faltantes
        pago_data = {
            'numero_tarjeta': '1234567890123456',
            'contrasena': 'password',
            'user_id': 1
        }

        response = self.client.post('/pago', json=pago_data)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Todos los campos son obligatorios')

    def test_pago_insufficient_balance(self):
        # Simular saldo insuficiente para la compra
        pago_data = {
            'numero_tarjeta': '1234567890123456',
            'fecha_vencimiento': '12/23',
            'contrasena': 'password',
            'user_id': 1
        }

        # Actualizar el saldo del cliente para que sea menor al precio del producto
        with self.dev.app.app_context():
            cliente = Clients.query.get(1)
            cliente.saldo = 200
            db.session.commit()

        response = self.client.post('/pago', json=pago_data)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Saldo insuficiente')

    def test_pago_error(self):
        # Simular un error en la transacción
        with self.dev.app.app_context():
            # Forzar un error al realizar la transacción
            def raise_error(*args, **kwargs):
                raise Exception('Error en la transacción')

            db.session.commit = raise_error

            # Simular datos válidos del formulario de pago
            pago_data = {
                'numero_tarjeta': '1234567890123456',
                'fecha_vencimiento': '12/23',
                'contrasena': 'password',
                'user_id': 1
            }

        response = self.client.post('/pago', json=pago_data)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Error en la transacción')
