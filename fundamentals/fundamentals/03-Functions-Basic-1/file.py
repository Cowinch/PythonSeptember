def multiply(num_list, num):
    for x in range(0,len(num_list),1):
        num_list[x]*=num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
# print(b)
# output:
# >>>[2,4,10,16]
#1
def number_of_food_groups():
    return 5
# print(number_of_food_groups()) 
#this prints 5 as an integer

#2
def number_of_military_branches():
    return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# this will cause an error as the function is not defined

#6
def add(b,c):
    print(b+c)
    return(b+c)
print(add(1,2) + add(2,3))
#return a non type error because no return assigns value to a function. otherwise its None

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

#14
# def foo():
#     print(1)
#     bar()
#     print(2)
# def bar():
#     print(3)
# foo()

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)


















