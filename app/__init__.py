from flask import Flask
from config import Config

# Create an instance of class Flask named app
app = Flask(__name__)
app.config.from_object(Config)

from app import routes
