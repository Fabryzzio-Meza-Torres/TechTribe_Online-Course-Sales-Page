#Imports
from flask import (
    Flask, 
    render_template, 
    request,
    jsonify,
    redirect, 
    url_for
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
import traceback
import os
from datetime import datetime,timedelta
import sys
import psycopg2
#Config 
dev=Flask(__name__)
dev.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mezatorres123@localhost:5432/project'
db= SQLAlchemy(dev)
migrate = Migrate(dev, db)

#Models
class Clients(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()), unique=True, nullable=False)
    firstname= db.Column(db.String(30), nullable=False)
    lastname= db.Column(db.String(50), nullable=False, unique=False)
    email= db.Column(db.String(99), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, server_default=db.text("now()"))
    
    def __init__(self, firstname, lastname, email):
        self.firstname= firstname
        self.lastname= lastname
        self.email= email
        self.modified_at = datetime.utcnow()
        self.created_at = datetime.utcnow()
    @classmethod
    def check_password(self, hashed_password,password):
        return check_password_hash(hashed_password, password)

class Trabajadores(db.Model):
    __tablename__ = 'workers'
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()), unique=True, nullable=False)
    firstname = db.Column(db.String(30), nullable=False,unique=False)
    lastname = db.Column(db.String(30), nullable=False, unique=True)
    age = db.Column(db.Integer, unique=False, nullable=False)
    especializacion= db.Column(db.String(30), nullable=False, unique=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, server_default=db.text("now()"))

    def __init__(self, firstname, lastname, age, especializacion):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.especializacion = especializacion
        self.modified_at = datetime.utcnow()
        self.created_at = datetime.utcnow()
    
class Producto(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()), unique=True, nullable=False)
    id_worker = db.Column(db.String(10), db.ForeignKey('workers.id'), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float(precision=2 ), nullable=False)
    type_product = db.Column(db.String(30), nullable=False)
    duration = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, server_default=db.text("now()"))

    def ___init___(self,id_worker, name, price, type_product, description, duration):
        self.id_worker = id_worker
        self.name = name
        self.price = price 
        self.type_product = type_product
        self.description = description
        self.duration = duration
        self.modified_at = datetime.utcnow()
        self.created_at = datetime.utcnow()

class Tarjeta(db.Model):
    __tablename__ = "credit_card"
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()), unique=True, nullable=False)
    creditcard_number = db.Column(db.String(20), nullable=False)
    expiration_date= db.Column(db.Date, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    id_client = db.Column(db.String(10),db.ForeignKey('clients.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, server_default=db.text("now()"))

    def __init__(self, creditcard_number, password, id_client):
        self.creditcard_number = creditcard_number
        self.expiration_date = timedelta(days=30,weeks=0,months=0,year=4) # rango de 4 años y un mes desde hoy
        self.password = password
        self.id_client = id_client
        self.modified_at = datetime.utcnow()
        self.created_at = datetime.utcnow()

class Orden_de_Compra(db.Model):
    __tablename__ = 'purchase_order'
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()), unique=True, nullable=False)
    product_name = db.Column(db.String(50), nullable=False)
    total_price = db.Column(db.Float(), nullable=False)
    id_product = db.Column(db.String(10), db.ForeignKey('products.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, server_default=db.text("now()"))

    def __init__(self, product_name,total_price):
        self.product_name = product_name
        self.total_price = total_price
        self.modified_at = datetime.utcnow()
        self.created_at = datetime.utcnow()


def crear_datos_por_defecto():
   with dev.app_context():
    trabajadores = Trabajadores.query.all()
    cursos = Producto.query.all()
    
    if not trabajadores:
        profesor1=Trabajadores("Marvin","Abisrror","25","Python")
        profesor2=Trabajadores("Jesus","Bellido","38","Python")
        profesor3=Trabajadores("Jose","Fiestas","35","C++")
        profesor4=Trabajadores("Ruben","Rivas","55","C++")
        profesor5=Trabajadores("Alan","Morante","42","HTML/CSS")
        profesor6=Trabajadores("Jorge","Villavicencio","38","HTML/CSS")
        profesor7=Trabajadores("Jose Miguel","Renom","38","Matematica para CS")
        profesor8=Trabajadores("Jorge","Tipe","35","Matematica para CS")
        db.session.add_all([profesor1,profesor2,profesor3,profesor4,profesor5,profesor6,profesor7,profesor8])

    if not cursos:
        profesor1=Trabajadores.query.filter_by(firstname="Marvin").first()
        profesor2=Trabajadores.query.filter_by(firstname="Jesus").first()
        profesor3=Trabajadores.query.filter_by(firstname="Jose").first()
        profesor4=Trabajadores.query.filter_by(firstname="Ruben").first()
        profesor5=Trabajadores.query.filter_by(firstname="Alan").first()
        profesor6=Trabajadores.query.filter_by(firstname="Jorge").first()
        profesor7=Trabajadores.query.filter_by(firstname="Jose Miguel").first()
        profesor8=Trabajadores.query.filter_by(firstname="Jorge").first()
        curso1=Producto(profesor1.id,"Curso Python", 350.00, "Curso", "6 semanas")
        asesoria1=Producto(profesor2.id,"Asesoria Python", 40.00, "Asesoria", "2 horas")
        curso2=Producto(profesor3.id,"Curso C++", 350.00, "Curso", "8 semanas")
        asesoria2=Producto(profesor4.id,"Asesoria C++", 40.00, "Asesoria", "2 horas")
        curso3=Producto(profesor5.id,"HTML/CSS", 150.00, "Curso", "2 semanas")
        asesoria3=Producto(profesor6.id,"Asesoria HTML/CSS", 40.00, "Asesoria", "2 horas")
        curso4=Producto(profesor7.id,"Matematica para CS", 400.00, "Curso", "10 semanas")
        asesoria4=Producto(profesor8.id,"Asesoria Matematica para CS", 40.00, "Asesoria", "2 horas")
        db.session.add_all([curso1,asesoria1,curso2,asesoria2,curso3,asesoria3,curso4,asesoria4])

    db.session.commit()
    db.session.close()


# Routes
@dev.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# ----------------------------------------------------------------
@dev.route('/profesores')
def get_profesores():
    conn = psycopg2.connect(
        host = "localhost",
        database = "project",
        user="postgres",
        password = "1234"
    )

    cur = conn.cursor()
    cur.execute("SELECT firstname, lastname, age, especializacion FROM workers")

    results = []
    for row in cur.fetchall():
        results.append({
            'firstname': row[0],
            'lastname': row[1],
            'age': row[2],
            'especializacion': row[3]
        })

    cur.close()
    conn.close()
    return jsonify(results)
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
            elif not email.endswith('@gmail.com'):
                errors.append('Ingrese un correo de Gmail válido')
            else:
                user = Clients.query.filter_by(email=email).first()
                if user:
                    errors.append('El correo electrónico ya ha sido registrado')

            if errors:
                return jsonify({'success': False, 'message': errors}), 400
            else:
                hash_contrasena = generate_password_hash(contrasena, salt_length=8)
                print(hash_contrasena)
                new_user = Clients(name, lastname, email, hash_contrasena)
                db.session.add(new_user)
                db.session.commit()
                return jsonify({'id': new_user.id, 'success': True, 'message': 'Usuario creado exitosamente'}), 200

        except Exception as e:
            print(e)
            print(sys.exc_info())
            db.session.rollback()
            return jsonify({'success': False, 'message': 'Error al crear usuario'}), 500

    return render_template('register.html')


@dev.route('/asesorias', methods=['GET'])
def asesoria():
    return render_template('index.html')
# Run the app
if __name__ == '__main__':
    dev.run(debug=True)
else:
    print('Importing {}'.format(__name__))