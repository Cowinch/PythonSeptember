#we DO NOT use camel casing in python. we use snakeCasing all lowercase, spaced out by _ underscores.

import random
# print(random.randint(2,5))

#numbers in python are not decimal friendly by default. they must be written as floats or ints
# num =25
# dec =4.2
# int_to_float = float(35)
# float_to_int = int(44.2)
# int_to_complex = complex(35)
# print(int_to_float)
# print(float_to_int)
# print(int_to_complex)
# print(type(int_to_float))
# print(type(float_to_int))
# print(type(int_to_complex))

# print("Hello " +str(42)) #numbers that are meant to become strings have to written as a string or with str() around the number
#in python, numbers have to be written as an integer or a float
stringNum = "26"
# print(15+int(stringNum))
#int is basicaly a parseInt from java. this is used to turn a string num into an integer

#Data types

#Primitive

#numbers
num=7 #this is an integer
dec=9.3#this is a float


#string
string="this is a string"
string2='this is also a string'


#boolean
#True or False
bool=True
bool2=False#in python, true or false MUST be capitalized


#composite
#lists (known as arrays in JS)
list=[1,2,3,4,5,6,-100]
list2=["bob","kyle","susan"]
#as usual, computers count from 0, so bob is 0 and susan is 2
name=list[1]
list[3]=7 #this changes the 4 into a 7
first_three=list[0:3] #the final number counts in human, not computer.
last_number=list[-1]#begins the array afterwards. -2 would print 5,6
# print(first_three)
# print(last_number)
# print(len(list)) 
#in python length of an array is a function, not a method
# print(max(list))
list.sort(reverse=False)
# print(list)
list.sort(reverse=True)
# print(list)


#dictionaries (known as objects in JS)
#{}
dog={
    'name':'Spot',
    'age':3,
    'color':'spotted',
    'favorite_food':'peanut butter'
}
# print(dog['name'])
# dog['name']='tiger'
# print(dog['name'])

# print(dog.get('name'))
# #this works just like print(dog['name'])

# print(dog.get('food'))
# #because we use .get this wont break the code, as there is no food key in the dictionary

# if "food" in dog:
#     print('he has food')
# else:
#     print('he does not have a favorite food')

# print(dog)
# del dog['favorite_food']
# print(dog)
fav_food=dog.pop('favorite_food')

dog.clear()
#this clears out the entire dictionary

#tuples