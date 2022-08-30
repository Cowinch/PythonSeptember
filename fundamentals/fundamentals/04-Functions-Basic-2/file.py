def countdown(num):
    list=[]
    for i in range(num,-1,-1):
        list.append(i)
    return list
print(countdown(5))
print('')

def print_and_return(val1, val2):
    print(val1)
    return(val2)
print(print_and_return(1,5))
print('')

def first_plus_length(list):
    return list[0]+(len(list))
print(first_plus_length([1,2,3,4,5]))
print('')

def values_greater_than_second(list):
    new_list=[]
    if len(list)<2:
        return False
    for num in range(0,len(list),1):
        if list[num]>list[1]:
            new_list.append(list[num])
    return new_list
print(values_greater_than_second([5,2,3,2,1,4]))
print('')

def length_and_value(size,value):
    list=[]
    for i in range(0,size):
        list.append(value)
    return list
print(length_and_value(4,7))