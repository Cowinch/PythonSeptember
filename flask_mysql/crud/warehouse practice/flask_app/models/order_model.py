from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask import Flask
from flask_app import app
from flask_app.models import user_model

class Order:
    def __init__(self, data) -> None:
        self.id=data['id']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.user_id=data['user_id']
    
    @classmethod
    def create(cls, data):
        query="INSERT INTO orders (user_id) VALUES (%(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query="SELECT * FROM orders JOIN users on orders.user_id=users.id;"
        results=connectToMySQL(DATABASE).query_db(query)
        if len(results) >0:
            all_orders=[]
            for row in results:
                this_order=cls(row)
                user_data={
                    **row,
                    'users_id': row['users.id'],
                    'created_at':row['created_at'],
                    'updated_at':row['updated_at']
                }
                this_user=user_model.User(user_data)
                this_order.customer=this_user
                all_orders.append(this_order)
            return all_orders
        return []
    
    @classmethod
    def get_by_id(cls,data):
        query="SELECT * FROM orders JOIN users on users.id = orders.user_id WHERE orders.id = %(id)s;"
        results=connectToMySQL(DATABASE).query_db(query,data)
        if len(results) < 1:
            return False
        # return cls(results[0]) #this is what we returned BEFORE we added the join
        row=results[0]
        this_order=cls(row)
        user_data={
            **row,
            'id': row['users.id'],
            'created_at':row['created_at'],
            'updated_at':row['updated_at']
        }
        customer=user_model.User(user_data)
        this_order.customer=customer
        return this_order
    
    @classmethod
    def delete(cls,data):
        query='DELETE FROM orders WHERE id=%(id)s'
        return connectToMySQL(DATABASE).query_db(query, data)