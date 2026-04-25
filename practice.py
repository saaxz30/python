
text = input('Enter anything :')
freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0)+1
# .get() fetches the value for an key 
"""
print(d.get("a"))          # gets the value of a 
print(d.get("b"))          # None because there is no value of b
print(d.get("b", 0))       # 0 (default value) sets default value """

print(freq)

lst = [23,23,89,0,3,3]
# y = lst.copy[2:4]  # TypeError: 'builtin_function_or_method' object is not subscriptable
x = lst[2:4]
print(x)

# sys.argv[n] ; n = number of the index of argument
# it is used to get input before running via arguments

"""
import sys
name = sys.argv[1]  # by default the file path hold 0th index,so we need to start from 1
print(name) """

# string manupulations
example = 'saravanan'
print(example[-2:])
formatted = f"{example.replace("sa","sn")} wrong name" # x.replace expects 2 args(old:new).
print(formatted)
splitted = example.split('r')[1] # x.split('delimiter')[n] ; n=1:everything after that,n=0:nothing
print(splitted)

full_name = 'saravanan deivasigamani'
initial = ''.join([word[0].upper() for word in full_name.split()])
print(initial)
wc = full_name.split()
print(len(wc))

def Validation():
    n=0
    valid_code = 0000
    entered_code = int(input('enter ur code :'))
    if valid_code == entered_code:
        print('Validation done')
    elif n<3:    
        if valid_code != entered_code:
            while n < 2:
                retry = int(input("enter correct code :"))
                if retry != valid_code:
                    print("Please retry")        
                elif retry == valid_code:
                    print("Validation done")
                    break
                n += 1
        elif n == 3:   
            print("you are out of max limit:3")         
Validation()

def sampleFor_args(*args): # to get multiple argumental values
    print(args)
sampleFor_args(34,78,90,88)
# **kwargs = key:value pair arguments
def sampleFor_kargs(**kwargs):
    print('key value pairs')
    for key,values in kwargs.items():
        print(f"{key}:{values}")

k = input('enter the key here :')
v = input('enter the value here :')        
sampleFor_kargs(k = v)
    

