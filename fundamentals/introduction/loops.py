# LOOPS
# FOR
"""
for ___ in ___ :
    pass

first blank is the iterative variable <-- will represent each single thing from the sequence we iterate over

second blank is the sequence.
"""

for i in range(5):
    # print(i)
    pass
# this prints 0-4 because computers count from 0
start = 0
stop = 5
step = 1
for i in range(start, stop, step):
    pass
# start is INCLUSIVE, will start at 0 in this case
# stop is EXCLUSIVE, will stop BEFORE 5 in this case
# step is the increment, will go 1 at a time

fruits = ['mango', 'banana', 'pears', 'lyches', 'dragon fruit', 'tomato']
for fruit in fruits:
    # print(fruit)
    pass
for i in range(len(fruits)):
    pass  # print(f"{i}): {fruits[i]}")

dog = {
    'name': 'Spot',
    'age': 3,
    'color': 'spotted',
    'favorite_food': 'peanut butter'
}

for prop in dog:
    pass  # print(prop)

for key in dog:
    pass # print(f"{key}: {dog[key]}")
# when we loop a dictionary, the iterative variable (prop in this case) is the KEY

dog_list = [
    {
        'name': 'Spot',
        'age': 3,
        'color': 'spotted',
        'favorite_food': 'peanut butter'
    },
    {
        'name': 'Fido',
        'age': 55,
        'color': 'grey/white',
        'favorite_food': 'applesauce and crickets'
    }
]
# for dog in dog_list:
#     print(f"{dog['name']} will now print out")
#     for key in dog: 
#         print(f"{key}: {dog[key]}")
#make this print without restating the name as its already stated

#break
for i in range (50,-1,-1):
    if i==10:
        continue
    if i==8:
        break
    print(i)
    #continue effectively means skip, where as break forces us to exit the iteration

# WHILE
i=0
while(i<10):
    # print(i)
    i+=1
#not much to talk about