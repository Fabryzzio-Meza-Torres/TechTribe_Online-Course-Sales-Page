from flask import (
    Flask,
    request,
    jsonify,
    abort
)
from .models import db, setup_db, Employee, Department, File
from flask_cors import CORS
from .users_controller import users_bp
from .authentication import authorize

import os
import sys


def create_app(test_config=None):
    app = Flask(__name__)
    with app.app_context():
        app.register_blueprint(users_bp)
        setup_db(app, test_config['database_path'] if test_config else None)
        CORS(app, origins=['http://localhost:8080'])

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        response.headers.add('Access-Control-Max-Age', '10')
        return response

# Routes
@dev.route('/', methods=['GET'])
def index():
    logged_in = request.cookies.get('logged_in')

    if logged_in == 'true':
        user_id = request.cookies.get('user_id')
        user_name = request.cookies.get('user_name')
        data = {'message': 'Usuario registrado', 'user_id': user_id, 'user_name': user_name}

        return render_template('index.html',  logged_in=logged_in, data=data) 
    else:
        return render_template('index.html')

@dev.route('/cursos', methods=['GET'])
def showcursos():
    consulta_precio= text("SELECT price FROM products")
    resultado= db.session.execute(consulta_precio)
    precios = [row[0] for row in resultado]

    logged_in = request.cookies.get('logged_in')

    if logged_in == 'true':
        user_id = request.cookies.get('user_id')
        user_name = request.cookies.get('user_name')
        data = {'message': 'Usuario registrado', 'user_id': user_id, 'user_name': user_name}

        return render_template('cursos.html',  logged_in=logged_in, data=data,  precios=precios)
    else:   
        return render_template('cursos.html', precios=precios)

@dev.route('/asesorias', methods=['GET'])
def showasesoria():
    logged_in = request.cookies.get('logged_in')
    consulta_precio= text("SELECT price FROM products")
    resultado= db.session.execute(consulta_precio)
    precios = [row[0] for row in resultado]


    if logged_in == 'true':
        user_id = request.cookies.get('user_id')
        user_name = request.cookies.get('user_name')
        data = {'message': 'Usuario registrado', 'user_id': user_id, 'user_name': user_name}

        return render_template('asesoria.html',  logged_in=logged_in, data=data, precios=precios) 
    else:
        return render_template('asesoria.html',precios=precios)


# ----------------------------------------------------------------
@dev.route('/profesores')
def get_profesores():
    workers_results = Trabajadores.query.all();
    out = []
    for result in workers_results:
        out.append({'firstname': result.firstname, 'lastname': result.lastname})

    return render_template('profesores.html', workers=out)

#----------------------------------------------------------------

@dev.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            name = request.form.get('nombres')
            lastname = request.form.get('apellidos')
            email = request.form.get('correo')
            contrasena = request.form.get('contrasena')
            campos_validar = ['nombres', 'apellidos', 'contrasena']
            errors = []
            for campo in campos_validar:
                if not request.form.get(campo):
                    errors.append(f'El campo {campo} es obligatorio')
            
            if not email:
                errors.append('Ingrese su correo electrónico')
            elif not email.endswith(('@gmail.com', '@hotmail.es', '@utec.edu.pe')):
                errors.append('Ingrese un correo de Gmail válido')
            elif not re.match(r'^(?=.*[a-zA-Z])(?=.*\d).{8,}$', contrasena):
                errors.append('La contraseña no cumple con los requisitos, debe ser alfanumérica y tener al menos 8 caracteres')
            else:
                user = Clients.query.filter_by(email=email).first()
                if user:
                    errors.append('El correo electrónico ya ha sido registrado')

            if errors:
                return jsonify({'success': False, 'message': errors}), 400
            else:
                hash_object = hashlib.sha256()
                hash_object.update(contrasena.encode('utf-8'))
                password_hash = hash_object.hexdigest()
                print(password_hash)
                new_user = Clients(name, lastname, email, password_hash)
                db.session.add(new_user)
                db.session.commit()
                return jsonify({'id': new_user.id, 'success': True, 'message': 'Usuario creado exitosamente'}), 200

        except Exception as e:
            print(e)
            print(sys.exc_info())
            db.session.rollback()
            return jsonify({'success': False, 'message': 'Error al crear usuario'}), 500

    return render_template('register.html')



@dev.route('/login', methods=['GET', 'POST'])
def login(): 
    if request.method == 'POST':
        email = request.form.get('correo')
        contrasena = request.form.get('contrasena')
        user = Clients.query.filter_by(email=email).first()
        
        if user:
            hash_object = hashlib.sha256()
            hash_object.update(contrasena.encode('utf-8'))
            password_hash = hash_object.hexdigest()
            
            if user.contrasena == password_hash:
                # Verificar la contraseña cumple con los requisitos
                if re.match(r'^(?=.*[a-zA-Z])(?=.*\d).{8,}$', contrasena):
                    response=jsonify({'success': True, 'message': 'Inicio de sesión exitoso'})
                    response.set_cookie('logged_in', 'true')
                    response.set_cookie('user_id', str(user.id))  # Agregar el ID del usuario a la cookie
                    response.set_cookie('user_name', str(user.firstname)) 


                    return response,200

                else:
                    return jsonify({'success': False, 'message': 'La contraseña no cumple con los requisitos'}), 400
            else:
                return jsonify({'success': False, 'message': 'Credenciales inválidas'}), 400
        else:
            return jsonify({'success': False, 'message': 'Usuario no encontrado'}), 400
        
    else:
        return render_template('login.html')



@dev.route('/logout', methods=['GET'])
def logout():
    response = redirect('/')
    response.delete_cookie('logged_in')
    response.delete_cookie('user_id')
    response.delete_cookie('user_name')
    return response


@dev.route('/orden_de_compra/<curso_name>', methods=['GET','POST'])
def orden_de_compra(curso_name):
    if request.method == 'GET':
        # Obtener el name del producto seleccionado
        product_name = curso_name
        product = Producto.query.filter_by(name=product_name).first()
        if product:
            product_name = product.name
            product_price = product.price
            product_type = product.type_product
        else:
            return jsonify({'success': False, 'message': 'Producto no encontrado'}), 400
            
        return render_template('orden.html', product_name=product_name, product_price=product_price, product_type=product_type)
    
@dev.route('/compra', methods=['GET', 'POST'])
def compra():
    if request.method == 'POST':
        # Obtener los datos del formulario
        creditcard_number = request.form.get('numero_tarjeta')
        expiration_date = request.form.get('fecha_vencimiento')
        password = request.form.get('contrasena')
        # Obtener el ID del cliente actualmente autenticado (puedes modificar esto según tu implementación de autenticación)
        logged_in = request.cookies.get('logged_in')
        user_id = request.cookies.get('user_id')
        monto= random.randint(300, 2000)
        # Validar los datos del formulario (puedes agregar más validaciones según tus requisitos)
        if not creditcard_number or not expiration_date or not password:
            return jsonify({'success': False, 'message': 'Todos los campos son obligatorios'}), 400

        # Crear una nueva instancia de la tarjeta
        try:
            new_tarjeta = Tarjeta(creditcard_number, expiration_date, password,user_id,monto )
            db.session.add(new_tarjeta)
            db.session.commit()
            return jsonify({'success': True, 'message': 'Transaccion realizada correctamente'}), 200
        
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({'success': False, 'message': 'Error en la transaccion'}), 500

    return render_template('compra.html')
