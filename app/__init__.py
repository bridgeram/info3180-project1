from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "GazaKey"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://Project1:EralixBain@localhost/Project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

UPLOAD_FOLDER = './app/static/uploads' 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'

app = Flask(__name__)
app.config.from_object(__name__)
from app import views
