from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

import os
SECRET_KEY = os.urandom(32)

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ssite.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

rec=0 
def autoIncrement(): 
 global rec 
 pStart = 1  
 pInterval = 1 
 if (rec == 0):  
  rec = pStart  
 else:  
  rec += pInterval  
 return rec

from subjapp import sroutes