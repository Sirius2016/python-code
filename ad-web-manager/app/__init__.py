from flask import Flask

app = Flask(__name__)

# Basic configuration for the Flask app
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['DEBUG'] = True

from app import routes