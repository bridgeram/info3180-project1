"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import *
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename
from forms import *
import datetime
from models import UserProfile


###
# Routing for your application.
###


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    # Instantiate your form class

    # Validate file upload on submit
    if request.method == 'POST':
        # Get file data and save to your uploads folder

        flash('File Saved', 'success')
        return redirect(url_for('home'))

    return render_template('upload.html')
    
    
@app.route('/Profile',methods=['GET','POST'])
def Profile():
    form=uploadForm()
    if request.method== "POST" and form.validate_on_submit():
        dateCreated=datetime.datetime.now()
        fname=form.firstname.data
        lname=form.lastname.data
        gen=form.gender.data
        email=form.email.data
        location=form.location.data
        bio=form.bio.data
        pic=form.photo.data
        filename = secure_filename(pic.filename)
        
        user = UserProfile(first_name=fname, last_name=lname, gender=gen, email=email, location=location, bio=bio, img_name=filename, date_created=dateCreated)
        db.session.add(user)
        db.session.commit()
        pic.save(os.path.join(imgfolder, filename))
        flash('Successfully added.', 'success')
        return redirect(url_for('Profiles'))
        
    
    return render_template('Profile.html',form=form)
    
@app.route('/Profiles')
def Profiles():
    image_names= get_uploaded_images()
    users = UserProfile.query.all()
    return render_template('Profiles.html', users=users, image_names=image_names)
    
@app.route('/Profile/<userid>')
def user_profile(userid):
    user = UserProfile.query.filter_by(id=userid).first()
    image_names= get_uploaded_images()
    return render_template('userprofile.html', user=user, image_names=image_names)

def get_uploaded_images():
    image_names= os.listdir(imgfolder)
    image=[]
    for x in image_names:
        a,b= x.rsplit(".",1)
        if b == "jpg" or b == "png":
            image.append(x)
    return image
###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
