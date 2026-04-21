import time 
"""
def add2nums(a,b):
    \""" Adds two numbers \""" # to give desc on hovering
    return a + b
print(add2nums(3,6))
result = add2nums(4,8)
print(result)

# A Fn can be procedural like below but by default it returns 'None'
# To return something we use return keyword which is in above Fn
def add(x,y):
    z = x+y
    print(z)
res = add(8,9)
print("result is", res)

# input stream: 
v = input("enter ur fav num ") # --> gets input and converts it to an string.
print(v)

#Conditional statement:
x = 3
if (x==3):
    print(x)
elif x == 4:
    print(x)
elif x<3 or x>4:
    print(x)
else:
    print('nothing')
#Match is like switch case in java
name = 'saravanan'
match name:
    case 'saravanan':
        print('it is saravanan')
    case 'madhavan':
        print('it is madhavan')
# Loops
# while loop
i = 1
while i<=4:
    print('hi' , end ='')
    j = 0
    while j<=3:
        print('hello' , end ='')
        j += 1
    i += 1
    print()"""
#for loop
data =[34,'sara',56,9.0,11.34,'nive']
z=1
while z < len(data):
    print(data[z])
    z += 1 
    
for x in data:
    print(x)
for y in range(1,11):
    print(y*2+1)
for patter in range(1,6):
    print('* ' * patter)
n = 5
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)

#continue and break
#continue --> skips and break --> breaks the loop.
for y in range(0,11):
    if y%3 == 0:
        continue
    print(y)
name = input('type ur name :')
if len(name)>=5:
    mask = name[2:len(name)-2]
    print('**'+mask+'**')
else:
    print(name + str(len(name)))

def reverse(name: str):
    for x in range(len(name)-1,-1,-1):
        print(name[x],end="")

#a = 0
"""def sleep_example():
    for a in range(0,100,5):
        time.sleep(seconds)
        print(f"The time increment is by 5 : {a}")
seconds = int(input("enter the delay u want :"))
sleep_example()"""

reverse('saravanan')

