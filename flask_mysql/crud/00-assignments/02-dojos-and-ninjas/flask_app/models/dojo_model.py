from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import ninja_model

class Dojo:
    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    
    @classmethod
    def get_all(cls):
        query="SELECT * FROM dojos;"
        results=connectToMySQL(DATABASE).query_db(query)
        # print(results)
        all_dojos=[]
        for row_from_db in results:
            dojo_instance= cls(row_from_db) #instantiates dog object from row in db
            all_dojos.append(dojo_instance) #adds instance to list of instances
        return all_dojos
    
    @classmethod
    def create(cls, data):
        query="INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_one(cls,data):
        query ="SELECT * FROM dojos LEFT JOIN ninjas on dojos.id=dojo_id WHERE dojos.id=%(id)s;"
        results=connectToMySQL(DATABASE).query_db(query, data)
        # print(results)
        if len(results) > 0: #this if statement purely exists to return a FALSE boolean value if nothing comes up for results
            dojo_instance=cls(results[0])
            ninja_list=[] #defining an empty index where we will store our individual Ninja dictionaries
            for row_from_db in results:
                ninja_data={
                    'id': row_from_db['ninjas.id'],
                    'first_name': row_from_db['first_name'],
                    'last_name': row_from_db['last_name'],
                    'age': row_from_db['age'],
                    'created_at': row_from_db['created_at'],
                    'updated_at': row_from_db['updated_at'],
                    'dojo_id': row_from_db['dojo_id'],
                }
                ninja_instance=ninja_model.Ninja(ninja_data) #this line instantiates a Ninja using the ninja_data from the dictionary
                
                ninja_list.append(ninja_instance) #this line of code is what adds ninjas to our list
                
            dojo_instance.list_of_ninjas =ninja_list #this line creates an attribrute is what we use to attach our ninja's info 
            print(dojo_instance)
            return dojo_instance
        return False