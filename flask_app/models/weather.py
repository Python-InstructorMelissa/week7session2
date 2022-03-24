from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Weather:
    db = 'favoriteImages'
    # db = 'craftsnh_favoriteImages'
    def __init__(self, data):
        self.id = data['id']
        self.city = data['city']
        self.conditions = data['conditions']
        self.temp = data['temp']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM forecast;'
        results = connectToMySQL(cls.db).query_db(query)
        temps = []
        for row in results:
            temps.append(cls(row))
        return temps

    @classmethod
    def getOne(cls, data):
        query = "SELECT * FROM forecast WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO forecast (city, conditions, temp, user_id) VALUES (%(city)s, %(conditions)s, %(temp)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE forecast SET city=%(city)s, conditions=%(conditions)s, temp=%(temp)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM forecast WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)