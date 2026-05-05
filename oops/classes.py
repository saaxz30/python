'class definition ---> run time creates the obj ---> which is used as methods or instances of the class'
'Every class in python inherits object class by default' #class connection(object):
class connection:
    # __init__ an method use to initialize the instance variables for an objects of the class.
    # and it is called by default when an obj is created
    def __init__(self,url,code):
        self.url = url
        self.code = code
    
    def class_caller():
        print('calling using the classname')
        
    def make_connection(self, error):
        print(f"connection established :{self.url}//staus code :{self.code} ErrorType :{error}")
    

con1 = connection("https//photoshield.io","200:ok")
con2 = connection("https//photoshield.io","404:server not found")
con1.make_connection("No Error") # --> connection.make_connection(con1) [internal working]
print(con1.make_connection("hii"))
connection.class_caller()

'-------------------Class Method---------------------'
# to work with class variables we craete class methods
# class variable is common for all the objects
class clsmethod:
    classname = "cls_method"
    @classmethod          # a decorater which is responsible for passing the class.
    def clsm(cls):
        return cls.classname
print(clsmethod.clsm()) # accessing using the class.
obj = clsmethod()
print(obj.clsm()) # accessing using the object.

'------------------Static method---------------------'
# to create an utility method inside the class and to be accessed by its obj.
class static_utility:
    @staticmethod
    def filtering(tup):
        return list(filter(lambda x : x*2 == 10, tup ))
jar = static_utility()
print(jar.filtering((23,78,90,34,5)))
