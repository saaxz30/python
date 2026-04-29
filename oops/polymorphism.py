'---------Duck typing----------'
# Diff classes having same method name with diff implementation and passing the obj of any the class  
# Into an another class in which the respective method got triggered is called duck typing.
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
'------------__str__()------------'
# used to print the value of the object 
class courier:
    def __init__(self,name,state,pincode):
        self.name = name
        self.state = state
        self.pincode = pincode
    def __str__(self):
        return f"{self.name}:{self.state}:{self.pincode}"
    
    def fromaddress(self):
        return f"From : {self.name},{self.state}--{self.pincode}"
    
    def toaddress(self):
        return f"To : {self.name},{self.state}--{self.pincode}"
    
obj = courier('sara','TN',1006087)
print(obj)
print(obj.toaddress())
obj2 = courier('Nive','JK',608704)
print(obj2)
'<|||--------------------------------------------------------------------------|||>'