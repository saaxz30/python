'----------------single level--------------'
class A:
    def f1(self):
        print('in class A')
class B(A):
    def f2(self):
        print('in class B')
obj = B()
obj.f1()
'---------------multilevel inheritance---------'
class C(B):
    def __init__(self):
        print('in class C init')
    def f3(self):
        print('in class C')
obj2 = C()
obj2.f1()
'---------------multiple inheritance------------'
class D(C,B,A):   #TypeError: Cannot create a consistent 'method resolution order'(MRO) for bases A, B, C
    def __init__(self):
        super().__init__() 
        # super() is used to call the methods of the parent class in side its methods or class
        print('in class D init')
    def f4(self):
        print('in class D')
obj3 = D()
B.f2(obj3)
