# Create the server
# Add a listener
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
# Run the server

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://cpkvbwbl:u0ufyU4MYfGcU9Fb6CNlYttMms1qcnx_@trumpet.db.elephantsql.com/cpkvbwbl"
db = SQLAlchemy(app)

from application import routes
