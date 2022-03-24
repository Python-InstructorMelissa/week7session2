

from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash, jsonify
from flask_app.models.user import User
import requests
from flask_cors import CORS

CORS(app)


@app.route('/images/nasa/')
def nasaImage():
    if 'user_id' not in  session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        user = User.getOne(data)
    return render_template('nasaImage.html', user = user)

@app.route('/images/looneyToones/')
def looneyImages():
    if 'user_id' not in  session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        user = User.getOne(data)
    return render_template('toons.html', user = user)