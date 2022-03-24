from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_app.models import favorite
from flask_app.models import weather

class User:
    db = 'favoriteImages'
    # db = 'craftsnh_favoriteImages'
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.username = data['username']
        self.password = data['password']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.favs = []
        self.forecasts = []

    def fullName(self):
        return f'{self.firstName} {self.lastName}'

    @staticmethod
    def validate(user):
        isValid = True
        query = 'SELECT * FROM user WHERE email = %(email)s;'
        results = connectToMySQL(User.db).query_db(query, user)
        if len(results) >= 1:
            isValid = False
            flash("That email is already in our database")
        if not EMAIL_REGEX.match(user['email']):
            isValid = False
            flash("Invalid email format")
        q = 'SELECT * FROM user WHERE username = %(username)s;'
        r = connectToMySQL(User.db).query_db(q, user)
        if len(r) >= 1:
            isValid = False
            flash("That username is already in use")
        if len(user['firstName']) < 2:
            isValid = False
            flash('Please use at least 2 characters for the first name')
        if len(user['lastName']) < 2:
            isValid = False
            flash('Please use at least 2 characters for the last name')
        if len(user['password']) < 8:
            isValid = False
            flash('Password must be at least 8 characters long')
        if user['password'] != user['confirm']:
            isValid = False
            flash('Passwords do not match')
        return isValid
    
    @staticmethod
    def validatePassword(user):
        isValid = True
        if len(user['password']) < 8:
            isValid = False
            flash('Password must be at least 8 characters long')
        if user['password'] != user['confirm']:
            isValid = False
            flash('Passwords do not match')
        return isValid

    @staticmethod
    def validateUpdate(user):
        isValid = True
        q = 'SELECT * FROM user WHERE username = %(username)s;'
        r = connectToMySQL(User.db).query_db(q, user)
        if len(r) >= 1:
            isValid = False
            flash("That username is already in use")
        if len(user['firstName']) < 2:
            isValid = False
            flash('Please use at least 2 characters for the first name')
        if len(user['lastName']) < 2:
            isValid = False
            flash('Please use at least 2 characters for the last name')
        return isValid

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM user;'
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def getOne(cls, data):
        query = "SELECT * FROM user WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def getLogin(cls, data):
        query = "SELECT * FROM user WHERE email = %(email)s OR username = %(username)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO user (firstName, lastName, email, username, password) VALUES (%(firstName)s, %(lastName)s, %(email)s, %(username)s, %(password)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def updateUser(cls, data):
        query = 'UPDATE user SET firstName=%(firstName)s, lastName=%(lastName)s, username=%(username)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def updatePassword(cls, data):
        query = 'UPDATE user SET password=%(password)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        pass

    @classmethod
    def userFavs(cls, data):
        query = 'SELECT * FROM user LEFT JOIN favorite ON user.id = favorite.user_id WHERE user.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        user = cls(results[0])
        for row in results:
            favoriteData = {
                'id': row['favorite.id'],
                'name': row['name'],
                'img': row['img'],
                'createdAt': row['favorite.createdAt'],
                'updatedAt': row['favorite.updatedAt'],
                'user_id': row['user_id'],
            }
            user.favs.append(favorite.Favorite(favoriteData))
        return user
    
    @classmethod
    def userForecasts(cls, data):
        query = 'SELECT * FROM  user LEFT JOIN forecast ON user.id = forecast.user_id WHERE user.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        theuser = cls(results[0])
        for row in results:
            forecastData = {
                'id': row['forecast.id'],
                'city': row['city'],
                'conditions': row['conditions'],
                'temp': row['temp'],
                'createdAt': row['forecast.createdAt'],
                'updatedAt': row['forecast.updatedAt'],
                'user_id': row['user_id'],
            }
            theuser.forecasts.append(weather.Weather(forecastData))
        return theuser