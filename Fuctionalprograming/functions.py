def sara(func):
    print('It\'s sara')
    return func()
def nive():
    return 'It\'s nive'
print(sara(nive))

assinging = nive
print(assinging)


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