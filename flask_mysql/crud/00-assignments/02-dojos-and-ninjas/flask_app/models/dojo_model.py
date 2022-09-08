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
        query ="SELECT * FROM dojos LEFT JOIN ninjas on dojos.id=dojo_id WHERE dojos.id=%(id)s"
        results=connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        if len(results) > 0:
            dojo_instance=cls(results[0])
            ninja_list=[]
            for row_from_db in results:
                ninja_data={
                    'id': row_from_db['ninjas.id'],
                    'first_name': row_from_db['first_name'],
                    'last_name': row_from_db['last_name'],
                    'age': row_from_db['age'],
                    'created_at': row_from_db['created_at'],
                    'updated_at': row_from_db['updated_at'],
                    'dojo_id': row_from_db['dog_id'],
                }
                dojo_instance=ninja_model.Assign(ninja_data)
                ninja_list.append(dojo_instance)
            dojo_instance.list =ninja_list
            return dojo_instance
        return False