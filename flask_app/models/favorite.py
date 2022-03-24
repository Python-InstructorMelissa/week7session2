from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Favorite:
    db = 'favoriteImages'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.img = data['img']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM favorite;'
        results = connectToMySQL(cls.db).query_db(query)
        favs = []
        for row in results:
            favs.append(cls(row))
        return favs

    @classmethod
    def getOne(cls, data):
        query = "SELECT * FROM favorite WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO favorite (name, img, user_id) VALUES (%(name)s, %(img)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE favorite SET name=%(name)s, img=%(img)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM favorite WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)