import os
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from authentication_service.interfaces.features.user.auth_command_routes import auth_command_routes
from authentication_service.interfaces.features.user.auth_quary_routes import auth_quary_routes
from authentication_service.infra.error_handling_middleware import ErrorHandlingMiddleware



# Load environment variables from .env file
load_dotenv('.env')

app = Flask(__name__)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

CORS(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.wsgi_app = ErrorHandlingMiddleware(app.wsgi_app)


@app.route('/')
def default_route():
    return "Welcome to the default route!"

# Register the authentication service routes
app.register_blueprint(auth_command_routes, url_prefix='/api/auth/command')
app.register_blueprint(auth_quary_routes, url_prefix='/api/auth/quary')

if __name__ == '__main__':
    app.run(port = 5000)
