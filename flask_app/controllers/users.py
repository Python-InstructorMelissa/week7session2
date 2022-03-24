from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.favorite import Favorite
from flask_app.models.weather import Weather


bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/', methods=['POST'])
def register():
    isValid = User.validate(request.form)
    if not isValid:  # if isValid = False then redirect to /
        return redirect('/')
    newUser = {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'email': request.form['email'],
        'username': request.form['username'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(newUser)
    if not id:
        flash('Something went wrong')
        return redirect('/')
    session['user_id'] = id
    flash("You are now logged in")
    return redirect('/dashboard/')

@app.route('/login/', methods=['POST'])
def login():
    data = {
        'email': request.form['email'],
        'username': request.form['username'],
    }
    user = User.getLogin(data) # check if the email is in the database
    if not user: # if not let them know
        flash('That email or username is not in our system')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Wrong password')
        return redirect('/')
    session['user_id'] = user.id
    flash("You are now logged in")
    return redirect('/dashboard/')

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')

@app.route('/profile/')
def editProfile():
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    user = User.getOne(data)
    return render_template('profile.html', user = user)

@app.route('/updateProfile/', methods=['post'])
def updateProfile():
    isValid = User.validateUpdate(request.form)
    if not isValid:
        return redirect('/profile/')
    id = session['user_id']
    updateUser = {
        'id': id,
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'username': request.form['username'],
    }
    User.updateUser(updateUser)
    return redirect('/profile/')

@app.route('/updatePassword/', methods=['post'])
def updatePassword():
    isValid = User.validatePassword(request.form)
    if not isValid:
        return redirect('/profile/')
    id = session['user_id']
    updateUser = {
        'id': id,
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    User.updatePassword(updateUser)
    flash('Password updated')
    return redirect('/profile/')

@app.route('/users/')
def users():
    if 'user_id' not in session:
        flash('please log in')
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    you = User.getOne(data)
    users = User.getAll()
    favs = Favorite.getAll()
    temps = Weather.getAll()
    return render_template('users.html', you = you, users = users, favs = favs, temps = temps)

@app.route('/users/<int:id>/view/')
def viewUser(id):
    if 'user_id' not in session:
        flash('please log in')
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    userData = {
        'id': id
    }
    you = User.getOne(data)
    user = User.getOne(userData)
    images = User.userFavs(userData)
    forecast = User.userForecasts(userData)
    return render_template('viewUser.html', you = you, user = user, images = images, forecast = forecast)
