from flask import Flask
from flask_sqlalchemy import SQLAlchemy

SECRET_KEY = 'Sup3r$3cretkey'
UPLOAD_FOLDER = './app/static/uploads'

app = Flask(__name__)
app.config['SECRET_KEY'] = "gaza"
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://awjlxxdgzsvced:34f93e2e57d7088421cb58704f5b840d28cd76a3d5bd46282b5a185f265d0b6d@ec2-54-204-44-140.compute-1.amazonaws.com:5432/dantits6675eai'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning


db = SQLAlchemy(app)


app.config.from_object(__name__)
imgfolder = app.config['UPLOAD_FOLDER']
app.debug= True
from app import views