#ive chosen not to do such massive numbers for my sanitys sake

print("Numbers 0-15")
for i in range(16):
    print(i)
print('')

print("multiples of 5, all the way to 100") 
for i in range(5,101, 5):
    print(i)
    print('')

print("Counting dojo style")
for i in range(1,101):
    if(i%10==0):
        print("Coding")
    elif (i%5==0):
        print("Coding Dojo")
    else:
        print(i)
print('')

print("Whoa. That sucker's huge")
sum=1
for i in range(3, 500001, 2):
    sum+=i
print(sum)
print('')

print("countdown by fours")
for i in range(2018, -1, -4):
    print(i)
print('')

print("Flexible Counter")
low_num=2
high_num=9
mult=3
for i in range(low_num,high_num+1):
    if(i%mult==0):
        print(i)
print('')