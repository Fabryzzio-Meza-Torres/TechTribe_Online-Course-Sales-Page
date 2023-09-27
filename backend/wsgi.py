from flask import Flask
from api1.app import dev as api1
from api2.app import dev as api2
from api3.app import dev as api3

def create_wsgi_app():
    app = Flask(__name__)

    # Registrar las APIs como Blueprints
    app.register_blueprint(api1, url_prefix='/api1')
    app.register_blueprint(api2, url_prefix='/api2')
    app.register_blueprint(api3, url_prefix='/api3')

    return app

application = create_wsgi_app()

if __name__ == '__main__':
    application.run()