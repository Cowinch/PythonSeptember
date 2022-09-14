from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask import Flask
from flask_app import app
from flask_app.models import user_model

class Recipe:
    def __init__(self,data) -> None:
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.instructions=data['instructions']
        self.under=data['under']
        self.date=data['date']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.user_id=data['user_id']
    
    @classmethod
    def create(cls, data):
        query="INSERT INTO recipes (name, description, instructions, under, date, user_id) VALUES (%(name)s,%(description)s,%(instructions)s,%(under)s,%(date)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query="SELECT * FROM recipes JOIN users on recipes.user_id=users.id;"
        results=connectToMySQL(DATABASE).query_db(query)
        if len(results) >0:
            all_recipes=[]
            for row in results:
                this_party=cls(row)
                user_data={
                    **row,
                    'id': row['users.id'],
                    'created_at':row['created_at'],
                    'updated_at':row['updated_at']
                }
                this_user=user_model.User(user_data)
                this_party.creator=this_user
                all_recipes.append(this_party)
            return all_recipes
        return []
    
    @classmethod
    def delete(cls,data):
        query='DELETE FROM recipes WHERE id=%(id)s'
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_by_id(cls,data):
        query="SELECT * FROM recipes JOIN users on users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        results=connectToMySQL(DATABASE).query_db(query,data)
        if len(results) < 1:
            return False
        # return cls(results[0]) #this is what we returned BEFORE we added the join
        row=results[0]
        this_recipe=cls(row)
        user_data={
            **row,
            'id': row['users.id'],
            'created_at':row['created_at'],
            'updated_at':row['updated_at']
        }
        creator=user_model.User(user_data)
        this_recipe.creator=creator
        return this_recipe
    
    @classmethod
    def update(cls,data):
        query="UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, under=%(under)s, date=%(date)s WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @staticmethod
    def validator(form_data):
        is_valid=True
        if len(form_data['name'])<1:
            flash('name of recipe required')
            is_valid=False
        if len(form_data['description'])<1:
            flash('description required')
            is_valid=False
        if len(form_data['instructions'])<1:
            flash('instructions required')
            is_valid=False
        if len(form_data['date'])<1:
            flash('date required')
            is_valid=False
        if "under" not in form_data:
            flash('please specify whether it is under 30 minutes to make or not')
            is_valid=False
        return is_valid