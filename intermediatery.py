from array import *

dictn ={}
def adding_records():
    n = int(input('enter the no:of:records you want to enter :'))
    i = 0
   # dictn = {}
    while i < n:
        key =  input("enter name :").lower()
        if key in dictn:
            print('Name already exist')
            continue
        values = int(input("enter age :"))
       #dictn.update({key:values})
        dictn[key] = values
        i += 1
    print(dictn)
# adding_records() 
d1 = {}
d1.update(dictn)
"""
students = [
    ("Sam", "A"),
    ("John", "B"),
    ("Ram", "A")
]
group = {}

for name, grade in students:
    if grade not in group:
        group[grade] = []   # create list
    
    group[grade].append(name)  # add to list
print(group)     """
#  array's are the form of list but with same data type and they are mutable aswell.
arr1 = array('i',[33,5,89,78,20])
arr2 = arr1
# print(hash(arr1)) --> TypeError: unhashable type: 'array.array'
if arr1 == arr2:
    print("They are refering the same obj")

arr = array('i')
n = int(input("No:Of:Data you want to enter :"))

for x in range(n):
    arr.append(int(input("enter data :")))
print(arr.tolist())    