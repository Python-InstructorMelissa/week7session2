import re
from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash, jsonify
from flask_app.models.weather import Weather
from flask_app.models.user import User
import requests
from flask_cors import CORS

CORS(app)


@app.route('/weather/')
def weather():
    if 'user_id' not in  session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        user = User.getOne(data)
    return render_template('weather.html', user = user)

@app.route('/weather/save/', methods=['post'])
def saveWeather():
    data = {
        'city': request.form['city'],
        'conditions': request.form['conditions'],
        'temp': request.form['temp'],
        'user_id': session['user_id']
    }
    Weather.save(data)
    return redirect('/dashboard/')
