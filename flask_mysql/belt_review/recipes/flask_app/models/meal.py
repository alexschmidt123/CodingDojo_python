from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template, redirect, request, session, flash
class Meal():

    def __init__(self,data):
        self.id = data['id']
        self.name =data['name']
        self.description =data['description']
        self.instruction =data['instruction']
        self.under_30_minute =data['under_30_minute']
        self.user_id = data['user_id']
        self.made_date = data['made_date']
        self.created_at =data['created_at']
        self.updated_at =data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO meals (name, description,instruction,under_30_minute, user_id, made_date) VALUES ( %(server_name)s,%(server_description)s,%(server_instruction)s,%(server_under_30_minute)s,%(server_user_id)s, %(server_made_date)s);"
        result = connectToMySQL("recipes").query_db(query,data)
        return result
        

    @classmethod
    def get_all_meals(cls):
        query = 'SELECT * FROM meals;'
        # query = 'SELECT * FROM meals WHERE user_id = %(server_user_id)s;'
        results = connectToMySQL('recipes').query_db(query)
        meals = []
        for each_result in results:
            meals.append( Meal(each_result) )
        return meals

    @classmethod
    def get_one_meal(cls,data):
        query = 'SELECT * FROM meals WHERE id =%(server_meal_id)s'
        results = connectToMySQL('recipes').query_db(query, data)
        return Meal(results[0])

    @classmethod
    def update_meal(cls,data):
        query = 'UPDATE meals SET name = %(server_name)s, description = %(server_description)s, instruction = %(server_instruction)s, made_date = %(server_made_date)s, under_30_minute=%(server_under_30_minute)s WHERE id = %(meal_id)s;'
        return connectToMySQL('recipes').query_db( query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM meals WHERE id = %(meal_id)s;'
        return connectToMySQL('recipes').query_db( query, data)

    @staticmethod
    def validate_new_meal(data):
        print(data)
        meal_is_valid = True
        if len(data['template_name']) < 3:
            meal_is_valid = False
            flash("name should be more than 2 characters long")
        if len(data['template_description']) < 3:
            meal_is_valid = False
            flash("description should be more than 2 characters long")
        if len(data['template_instruction']) < 3:
            meal_is_valid = False
            flash("instruction should be more than 2 characters long")
        if 'template_under_30_minute' not in data:
            meal_is_valid = False
            flash("Check box should be checked")
        if data['template_made_date'] == "":
            meal_is_valid = False
            flash("Made date should be input")

        return meal_is_valid


