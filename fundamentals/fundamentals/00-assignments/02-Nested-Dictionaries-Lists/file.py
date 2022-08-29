x = [[5, 2, 3], [10, 8, 9]]  # nested list
students = [  # nested dictionaries
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]
x[1][0] = 15
# print(x)

students[0]['last_name'] = "Bryant"
# print(students[0])

sports_directory['soccer'][0] = 'Andres'
# print(sports_directory['soccer'])

z[0]['y'] = 30
# print(z)

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(list):
    for i in range(0, len(list), 1):
        print(
            f"first_name - {list[i]['first_name']}, last_name - {list[i]['last_name']}")
        print('')

# iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


def iterateDictionary2(key_name, some_list):
    for i in range(0, len(some_list), 1):
        print(some_list[i][key_name])
# iterateDictionary2('first_name', students)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    print(f"{len(dojo['locations'])}  Locations")
    for i in range(0, len(dojo['locations']), 1):
        print(dojo['locations'][i])
    print('')
    print(f"{len(dojo['instructors'])}  instructors")
    for i in range(0, len(dojo['instructors']), 1):
        print(dojo['instructors'][i])
    print('')


printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
