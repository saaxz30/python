def sara(func):
    print('It\'s sara')
    return func()
def nive():
    return 'It\'s nive'
# print(sara(nive)) # passing the fn as an argument. 

res = f"{sara(nive)} \n inside result for fn returned storage" # where the value which is returned by the fn is stored
print(res)
assigning = nive  # fn is assigned to an variable which can be also celled as an fn.
print(assigning()) 


class demo:

    def example(self,x,y):
        self.comparison_value = x
        self.comparing_value = y
        if self.comparison_value > self.comparing_value :
            print(f"{self.comparison_value} is grater")
        else:
            print(f"{self.comparing_value} is grater")

obj = demo()
print(demo.example(obj,35,89))
print(obj.example(76,56))

class phone:
    pass
obj2 = phone()
print(obj2)