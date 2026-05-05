'what is abstraction?'
# Hiding the complex thing and just making the implementation of the abstract class is called 'Abstraction'.
# Note: We can't create the object of an abstract class and abstract method should be an part of abs-cls.
# And abstract method can't be defined
'How do we implement it?'
# By inheriting ABC class and by decorating it with @abstractmethod

from abc import ABC,abstractmethod

class payment_gateway(ABC):
    @abstractmethod
    def pay(self):
        pass
class razorpay(payment_gateway):
    def pay(self):
        print("paying using razorpay")
class stipe(payment_gateway):
    def pe(self):
        print("paying using sripe")

class purchase:

    def __init__(self,gateway):
        self.gateway = gateway

    def checkout(self):
        print("checking out...")
        self.gateway.pay()

gateway = stipe()
purchases = purchase(gateway) 

purchases.checkout()

"""
self.gateway.pay() calls the pay method on the gateway attribute of the current object instance.
In other words, self refers to the current object, gateway is an attribute on that object, 
and pay() is invoked on whatever object is stored there.
Because gateway is an object, this is a dynamic method call: 
Python looks up gateway on self, finds its class, then executes that class’s pay implementation.
In the provided implementation, that results in printing "Paid amount xxxxx".
"""

"""dict = {}

def demo():
    n = int(input())
    for n in range(0,n):
        keys = input()
        values = input()
        dict[keys] = values
demo()
print(dict)"""

