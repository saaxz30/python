class construct:
    def __new__(cls):   #obj.message() AttributeError: 'NoneType' object has no attribute 'message'
        print('constructor caller')
        return super(construct,cls).__new__(cls)

    def __init__(self):
        print('in init method')

    def message(self):
        print('message card')

obj = construct()
obj.message()

obj2 = construct.__new__(construct)
obj2.message()
