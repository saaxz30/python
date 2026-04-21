
dictn ={}
def adding_records():
    n = int(input('enter the no:of:records you want to enter :'))
    i = 0
   # dictn = {}
    while i < n:
        key = input("enter name :")
        if key in dictn:
            print('Name already exist')
            continue
        values = int(input("enter age :"))
       #dictn.update({key:values})
        dictn[key] = values
        i +=1
    print(dictn)
adding_records() 
d1 = {}
d1.update(dictn)

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
print(group)    