from flask import *
from flask_restful import *
from firebase import *
import firebase
from firebase_admin import *
import firebase_admin
from pyrebase import *
import pyrebase
from pymongo import *
import json

app = Flask(__name__)
app.debug = True
app.secret_key = "RANUGA D 2008"
api = Api(app)
from server.routes import *