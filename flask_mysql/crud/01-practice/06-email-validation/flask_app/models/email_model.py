from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Email:
    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        
    def __repr__(self) -> str:
        return f'self.name'
    
    @classmethod
    def create(cls, data):
        query="INSERT INTO emails (name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query= "SELECT * FROM emails;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_emails = []
        for row in results:
            all_emails.append( cls(row) )
        return all_emails
    
    @classmethod
    def get_latest(cls):
        query='select * from emails order by id desc limit 1;'
        results = connectToMySQL(DATABASE).query_db(query)
        return results
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @staticmethod
    def validator(data):
        is_valid=True
        query = "SELECT * FROM emails WHERE name = %(name)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        if len(data['name'])<=0:
            flash('email is required','error_emails_name')
            is_valid=False
        if len(results) >= 1:
            flash('email is already taken', 'error_emails_name')
            is_valid=False
        elif not EMAIL_REGEX.match(data['name']):
            flash('Invalid email address', 'error_emails_name')
            is_valid=False
        if is_valid==True:
            flash('Successful email inserted!', 'success')
        return is_valid