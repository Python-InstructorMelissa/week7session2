from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.note import Note
from flask_app.models.user import User

@app.route('/dashboard/')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        user = User.getOne(data)
        notes = Note.getAll()
        # print('user.level: ', user.level)
        return render_template('dashboard.html', user=user, notes=notes)

@app.route('/note/create/', methods=['POST'])
def createNote():
    data = {
        'note': request.form['note'],
        'private': request.form['private'],
        'user_id': request.form['user_id'],
    }
    Note.save(data)
    flash('Note created')
    print("printing data save from note controller: ", data)
    return redirect('/dashboard/')