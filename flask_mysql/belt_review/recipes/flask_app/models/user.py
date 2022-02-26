from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

import re

class User():

    def __init__(self,data):
        self.id = data['id']
        self.first_name =data['first_name']
        self.last_name =data['last_name']
        self.email =data['email']
        self.password =data['password']
        self.created_at =data['created_at']
        self.updated_at =data['updated_at']

    @classmethod
    def create_new_user(cls,data):

        query = "INSERT INTO users (first_name, last_name, email, password) VALUES ( %(first_name)s,%(last_name)s,%(email)s,%(password)s);"

        result = connectToMySQL("recipes").query_db(query,data)

        return result
    
    # @classmethod
    # def get_user_by_username(cls,data):
    #     print(f'data: {data}')
    #     query ="SELECT * FROM users WHERE first_name = %(first_name)s AND last_name = %(last_name)s;"

    #     results = connectToMySQL("recipes").query_db(query,data)
    #     print(f'results: {results}')
    #     if len(results) == 0:
    #         return False
    #     else:
    #         return User(results[0])
    
    @classmethod
    def get_user_by_email(cls,data):
    
        query ="SELECT * FROM users WHERE email = %(email)s;"

        results = connectToMySQL("recipes").query_db(query,data)

        if len(results) == 0:
            return False
        else:
            return User(results[0])

    @staticmethod
    def validate_new_user(data):
        is_valid = True

        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        # username does not have to be unique
        # if User.get_user_by_username(data):
        #     is_valid = False
        #     flash("Username should be unique.")
        # username has 3-50 characters
        if len(data['first_name']) < 2 or len(data['first_name'])> 45:
            is_valid = False
            flash("First name should be 2 to 45 characters long")
        
        if len(data['last_name']) < 2 or len(data['last_name'])> 45:
            is_valid = False
            flash("Last name should be 2 to 45 characters long")
        


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
        if data['password'] != data['confirm_password']:
            is_valid = False
            flash("Password and confirm password do not match")

        return is_valid

