from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,validators, SelectField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired

from wtforms.validators import InputRequired

class uploadForm(FlaskForm):
    
    firstname = StringField('FirstName', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    gender = SelectField('Gender',choices=[('',"CHOOSE GENDER"),('male','Male'),('female','Female')] ,validators=[validators.Required("Gender Must be specified")])
    email= StringField('Email', validators=[InputRequired()])
    location=StringField('Location',validators=[InputRequired()])
    bio = TextAreaField('Biography', validators=[InputRequired()])
    photo = FileField('Profile Picture', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])