from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Joke:
    db = 'user'
    def __init__(self, data):
        self.id = data['id']
        self.jokeType = data['jokeType']
        self.jokeText = data['jokeText']
        self.jokeSetup = data['jokeSetup']
        self.jokeDeleiver = data['jokeDeleiver']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']

    @classmethod
    def getAll(cls):
        pass

    @classmethod
    def getOne(cls, data):
        pass

    @classmethod
    def saveSingle(cls, data):
        query = "INSERT INTO joke (jokeType, jokeText, user_id) values (%(jokeType)s, %(jokeText)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def saveTwopart(cls, data):
        query = "INSERT INTO joke (jokeType, jokeSetup, jokeDeleiver, user_id) values (%(jokeType)s, %(jokeSetup)s, %(jokeDeleiver)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)