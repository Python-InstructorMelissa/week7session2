from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_app.models.joke import Joke

@app.route('/dashboard/')
def dashboard():
    if 'user_id' not in session:
        flash('Hey there log in first dude!!!')
        return redirect('/')
    userData = {
        'id': session['user_id']
    }
    theUser = User.getOne(userData)
    return render_template('dashboard.html', user=theUser)

@app.route('/joke/')
def joke():
    if 'user_id' not in session:
        flash('Hey there log in first dude!!!')
        return redirect('/')
    userData = {
        'id': session['user_id']
    }
    theUser = User.getOne(userData)
    theJokes = User.userJokes(userData)
    print('users saved Jokes: ', theJokes)
    return render_template('joke.html', user=theUser)

@app.route('/joke/createSingle/', methods=['post'])
def createSingle():
    data = {
        'jokeType': request.form['jokeType'],
        'jokeText': request.form['jokeText'],
        'user_id': session['user_id']
    }
    Joke.saveSingle(data)
    flash("You saved this single part joke")
    return redirect('/joke/')

@app.route('/joke/createTwopart/', methods=['post'])
def createTwopart():
    data = {
        'jokeType': request.form['jokeType'],
        'jokeSetup': request.form['jokeSetup'],
        'jokeDeleiver': request.form['jokeDeleiver'],
        'user_id': session['user_id']
    }
    Joke.saveTwopart(data)
    flash("You saved this two part joke")
    return redirect('/joke/')