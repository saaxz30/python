""" def sample_fn():
    if 5>2:
        print("5 is greater than 2")

if __name__ == "__main__":
    sample_fn()

sample_fn() """

print(8**10)
"""
// - to get qoutient
/ - to get float value
% - to get reminder

"""
print('hello world')
print(5+7)
2 + 7 * 8 # no error will occur as python works as an scripting language with shell.
print(4//3)
nums =[1,2,3]
text = ['sara','nive','sarvedhitha']
# LIST : which is collection of values and it can hold values of diff types
# also we can have list of lists like mix = [nums,text] in which nums = 0 and text = 1
# to get into either nums or text we need [x][y] matrix of indexing to get the element
# has in-built fn's like .remove - removes by value, .pop - removes by index {LIFO}
# .insert(u,v) - inserts something after u = index : v = value.
mixedlist = nums + text
print(mixedlist.append(45))
print(mixedlist)
print('sara\'s') 
# to nullify special literls like "" ,'' , \ , \n ...etc 
# In print statement we use \ backslash to nullify syntax error
note = """
Hi everyone 
Good morning
"""
print(note[2:])
print(note[3:7])
#slicing i.e: [x:y] where x is included and y is excluded
# [x:] goes till end from x index
# [:y] starts from 0 index and goes till y-1 index
# we can also minus indexing in python which is helpfull for example if you want to print 
# let's say last 'n' in saravanan we can use -1 
# as indexing goes for saravanan in minus order like -1 to -9
name = 'saravanan'
print(name.upper())
print(name[-1]) 
print(len(name))
example_for_del = [3,4,5,6,7,8]
# print(list(example_for_del))
del(example_for_del[3:]) 
# del() is fn which deletes data from x index to y
print(example_for_del)
#Tuple: it's an immutable form of list where we can create a tuple by () or by default 
# multiple values implicitly becomes tuple which is called as packing.
# has .index(value) & .count(value) fn's
tuple_example = 23,'git','docker','aws',12
print(tuple_example.index('docker')) # ==> output: 2
a,b,*c,d = tuple_example
print(a,b,c,d, sep='\n')
from  datetime import datetime
now = datetime.now()
print(f"Today is {now:%d-%m-%y}")
#Set: collection of uniqe unordered data every value is stored based on hash value.
set_example = {23,56,90,3,5,8,23}
print(set_example)
# set as mathametical fn we can make union,inersection
set1 = set("a,b,c,d h,k,e,o")
set2 = set("b,c,m,j,h,u,i,t")
print(set1-set2)
print(set1|set2 ,'\n', set1&set2 ,'\n' , set1^set2)
# | --> like union all , & --> like intersection , -(minus) --> like differntial values

#Dictionary: A key - value pair data structure eg: dict = {x:y} where x is the key and y is value 
dictionary = {'sara':(23,33),'nive':21}
#print(dictionary.items())
items = dictionary.items()
print(items)
# while a key is not fetchable we can pass default value.
print(dictionary.get('sri','not found'))
# keys and values matching
keys = ['sara','nive','sri']
values = [23,21,18]
d = dict(zip(keys,values))
print(d)
# variables are container object with specific values and the same obj may have 
# multiple ref variables 
a = 5  
b = 6 
def checking_id():
    if (id(a) == id(b)):
        print('They are referencing same object')
    else:print('No they are different object')
checking_id()
        
print(id(a),id(b)) #here; id of a = id of b.
# python also haves garbage collection like java where it cleans up the object's
# which are not being refered 
type(a) # fn for finding the type of an obj
# to do type convertion we use fn like int(),float(),double()...
#Range: used for creating an range with G:F = range(n,n-1,i)
#where;n --> starting point ,n-1 --> ends here , i - iterable steps it follows.
print(list(range(1,11)))
"""
The module is an file which can be imported into another file for using its functions 
within the package and if the module is outside of the scope of the module then we need to 
import it with package name i,e: from package.module import *
"""
# And to make the block for execution of fn called in the same file in an imported file 
# We can use if(condition) like if __name__ == "__main__": and we can call those fn inside the
# If block to make it executable only when the actual file is runned.
