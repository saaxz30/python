'---------Duck typing----------'
# Diff classes having same method name with diff implementation and passing the obj of any of the class  
# into an another class in which the respective method got triggered is called duck typing.
class mobile_phone:
    def rings(self):
        print('mobile rings')
class landline_phone:
    def rings(self):
        print('landline rings')
class call:
    def call_reciver(self,ringing:mobile_phone):
        ringing.rings()

mobile = mobile_phone()
landline = landline_phone()
calls = call()
calls.call_reciver(mobile)
calls.call_reciver(landline)
'------------__str__()------------METHOD OVERLOADING-------------------__str__()--------------------------'
# used to print the value of the object (it's an inbuilt method)
class courier:
    def __init__(self,name,state,pincode):
        self.name = name
        self.state = state
        self.pincode = pincode
    def __str__(self):  #overrided
        return f"{self.name}:{self.state}:{self.pincode}"
    
    def fromaddress(self):
        return f"From : {self.name},{self.state}--{self.pincode}"
    
    def toaddress(self):
        return f"To : {self.name},{self.state}--{self.pincode}"
    
obj = courier('sara','TN',1006087)
print(obj.__str__())   #---> '<__main__.courier object at 0x0000024FDFB88AD0>'
# overridding this default method is called method overridding
print(obj.toaddress())
obj2 = courier('Nive','JK',608704)
print(obj2)
'<|||--------------------------------------------------------------------------|||>'
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()

make_sound(Dog())
make_sound(Cat())