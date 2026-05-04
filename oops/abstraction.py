class payment_gateway:
    def pay(self):
        print("Paid amount 12****00")
class purchase:

    def __init__(self,gateway):
        self.gateway = gateway

    def checkout(self):
        print("checking out...")
        self.gateway.pay()

print(gateway = payment_gateway())
#purchases = purchase(gateway) 

#purchases.checkout()

"""
self.gateway.pay() calls the pay method on the gateway attribute of the current object instance.
In other words, self refers to the current object, gateway is an attribute on that object, 
and pay() is invoked on whatever object is stored there.
Because gateway is an object, this is a dynamic method call: 
Python looks up gateway on self, finds its class, then executes that class’s pay implementation.
In the provided implementation, that results in printing "Paid amount xxxxx".
"""