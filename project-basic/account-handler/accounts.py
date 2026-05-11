from user import *



class account(users):
    def __init__(self):
        super().__init__()
        self.savings = "savings account"
        self.salary = "salary account"
    def create_accounts(self):
       pass

    def account_details(self, name):
        if name in self.user_list:
            print(f"""
            Name: {name}
            Account Type: {self.savings}
            """)
        else:
            print("User not found")

        
    #AttributeError: 'function' object has no attribute 'user'
    #AttributeError: 'account' object has no attribute 'user'          
                                      
        
    
acc_type = account()
#acc_type.account_type()
acc_type.add_user("sara",'nive')
acc_type.account_details('sara')