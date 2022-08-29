import random

# print('Welcome to Python!')

# print('This is a loop printing 5 times')
# for x in range(1, 6):
#     print(f'x is: {x}')

# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# day = random.choice(weekdays)

# print(f'Today is: {day}')

# if day == 'Monday':
#     print('It will be a long week!')
# elif (day == 'Friday'):
#     print('Woohoo, time for the weekend!')
# else:
#     print('Not quite there yet.')

# len is for length
dec = 4.2

# Data types

# Primitive

# numbers
num = 7  # this is an integer
dec = 9.3  # this is a float


# string
string = "this is a string"
string2 = 'this is also a string'


# boolean
#True or False
bool = True
bool2 = False  # in python, true or false MUST be capitalized


# composite
# lists (known as arrays in JS)
list = [1, 2, 3, 4, 5, 6, -100]
list2 = ["bob", "kyle", "susan"]
# as usual, computers count from 0, so bob is 0 and susan is 2
name = list[1]
list[3] = 7  # this changes the 4 into a 7
first_three = list[0:3]  # the final number counts in human, not computer.
last_number = list[-1]  # begins the array afterwards. -2 would print 5,6
# print(first_three)
# print(last_number)
# print(len(list))
# in python length of an array is a function, not a method
# print(max(list))
list.sort(reverse=False)
# print(list)
list.sort(reverse=True)
# print(list)


# dictionaries (known as objects in JS)
# {}
dog = {
    'name': 'Spot',
    'age': 3,
    'color': 'spotted',
    'favorite_food': 'peanut butter'
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
fav_food = dog.pop('favorite_food')
# this clears out the entire dictionary

# tuples
# tuples are IMUTABLE lists they CANNOT be changed
tuple = (1, 2, 3, 4, 5, 6)
# tuple[3]=7 would cause an ERROR

# conditionals

# if, else, elif (else if) you have to write it as elif


# if 'age' in dog:
#     print(f"Dog is {dog['age']}")

# if 'age' not in dog:
#     print("Dog doesn't have an age")
# elif dog['age'] > 4:
#     print("Dog is older than 4")
# else:
#     print("Dog is younger than 4")
