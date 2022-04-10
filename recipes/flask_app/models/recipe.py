from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    db_name = 'recipes'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.description = db_data['description']
        self.instructions = db_data['instructions']
        self.under30 = db_data['under30']
        self.date_made = db_data['date_made']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO recipes (name, description, instructions, under30, date_made, user_id) VALUES (%(name)s,%(description)s,%(instructions)s,%(under30)s,%(date_made)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_recipes = []
        for row in results:
            print(row['date_made'])
            all_recipes.append( cls(row) )
        return all_recipes
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, under30=%(under30)s, date_made=%(date_made)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters","recipe")
        if len(recipe['instructions']) < 3:
            is_valid = False
            flash("Instructions must be at least 3 characters","recipe")
        if len(recipe['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters","recipe")
        if recipe['date_made'] == "":
            is_valid = False
            flash("Please enter a date","recipe")
        return is_valid