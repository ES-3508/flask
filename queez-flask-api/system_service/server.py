import os
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS

from interfaces.routes import auth_app

# Load environment variables from .env file
load_dotenv('.env')

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/')
def default_route():
    return "Welcome to the default route!"

# Register the authentication service routes
app.register_blueprint(auth_app, url_prefix='/api/auth')

if __name__ == '__main__':
    app.run()
