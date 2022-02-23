from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

import re

class User():

    def __init__(self,data):
        self.id = data['id']
        self.username =data['username']
        self.email =data['email']
        self.password =data['password']
        self.created_at =data['created_at']
        self.updated_at =data['updated_at']

    @classmethod
    def create_new_user(cls,data):

        query = "INSERT INTO users (username, email, password) VALUES ( %(username)s,%(email)s,%(password)s);"

        result = connectToMySQL("login_demo").query_db(query,data)

        return result
    
    @classmethod
    def get_user_by_username(cls,data):
        print(f'data: {data}')
        query ="SELECT * FROM users WHERE username = %(username)s;"

        results = connectToMySQL("login_demo").query_db(query,data)
        print(f'results: {results}')
        if len(results) == 0:
            return False
        else:
            return User(results[0])
    
    @classmethod
    def get_user_by_email(cls,data):
    
        query ="SELECT * FROM users WHERE email = %(email)s;"

        results = connectToMySQL("login_demo").query_db(query,data)

        if len(results) == 0:
            return False
        else:
            return User(results[0])

    @staticmethod
    def validate_new_user(data):
        is_valid = True

        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        # username is not in use
        if User.get_user_by_username(data):
            is_valid = False
            flash("Username should be unique.")
        # username has 3-50 characters
        if len(data['username']) < 3 or len(data['username']) > 50:
            is_valid = False
            flash("Username should be 3 to 50 characters long")

        # email is not in use
        if User.get_user_by_email(data):
            is_valid = False
            flash("Email address should be unique")
        # email is valid
        if not email_regex.match(data['email']):
            is_valid = False
            flash("Email address is not formatted correctly")

        # password is of minimum length
        if len(data['password']) < 8:
            is_valid = False
            flash("Password should be at least eight characters long.")
        # password and comfirmed password match
        if data['password'] != data['confirmed_password']:
            is_valid = False
            flash("Password and confirmed password do not match")

        return is_valid

