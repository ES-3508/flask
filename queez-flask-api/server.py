import os
import sys
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from marketplace_com_service.interfaces.features.landing.landing_quary_routes import landing_quary_routes
from marketplace_com_service.interfaces.features.landing.landing_command_routes import landing_command_routes
from marketplace_com_service.infra.error_handling_middleware import ErrorHandlingMiddleware

from authentication_service.interfaces.features.user.auth_command_routes import auth_command_routes
from authentication_service.interfaces.features.user.auth_quary_routes import auth_quary_routes
from authentication_service.infra.error_handling_middleware import ErrorHandlingMiddleware

from marketplace_com_service.interfaces.features.advertisement.advertisement_command_routes import advertisement_command_routes
from marketplace_com_service.interfaces.features.advertisement.advertisement_quary_routes import advertisement_query_routes
# from authentication_service.interfaces.features.user.auth_command_routes import auth_command_routes
from marketplace_com_service.interfaces.features.customer_portal.customer_portal_command_routes import customerportal_command_routes
from marketplace_com_service.interfaces.features.customer_portal.customer_portal_quary_routes import customerportal_query_routes

load_dotenv('.env')

app = Flask(__name__)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate",
        'supportedSubmitMethods': ['get', 'post', 'put', 'delete'],
        'securityDefinitions': {
            'BearerAuth': {
                'type': 'apiKey',
                'in': 'header',
                'name': 'Authorization'
            }
        },
        'security': [{'BearerAuth': []}]
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

CORS(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.wsgi_app = ErrorHandlingMiddleware(app.wsgi_app)


@app.route('/')
def default_route():
    return "Welcome to the default route!"

app.register_blueprint(auth_command_routes, url_prefix='/api/auth/command')
app.register_blueprint(auth_quary_routes, url_prefix='/api/auth/quary')

app.register_blueprint(landing_quary_routes, url_prefix='/api/landing/quary')
app.register_blueprint(landing_command_routes, url_prefix='/api/landing/command')

# Registering advertisement routes
app.register_blueprint(advertisement_query_routes, url_prefix='/api/advertisement/quary')
app.register_blueprint(advertisement_command_routes, url_prefix='/api/advertisement/command')

app.register_blueprint(customerportal_query_routes, url_prefix='/api/customerportal/quary')
app.register_blueprint(customerportal_command_routes, url_prefix='/api/customerportal/command')

if __name__ == '__main__':
    app.run(debug=True)
    
    
