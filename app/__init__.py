from flask import Flask

# Create an instance of class Flask named app
app = Flask(__name__)

from app import routes
