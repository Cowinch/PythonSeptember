"""
    step 1: connection to the db - mysql
    the instance of the MySQLConnection class
    
    step 2: query string - 'INSERT INTO...'
    the string that will eventually be executed on our mySQL server
    
    step 3: data dictionary
    the values that will be interpolated into the query string
    
    step 4: data dictionary keys - first_name, last_name, email
    the keys of the data dictionary used in the query string with %-interpolation (%(key_name)s)
"""
#Example code

#step 2
query = "INSERT INTO friends (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s );"

#step 3
data = {
    #step 4
    "first_name" : "Adrien",
    "last_name" : 'Dion',
    'email' : 'adion@codingdojo.com'
}
#under no circumstance are we to use f strings or bypass making a dictionary. EVER! This leaves the database open to simple "SQL Injections" ie joe@gmail.com' or '1'='1  since 1=1 is always true this malicous user just fetched our ENTIRE QUERY.

#step 1
mysql.query_db(query, data)
