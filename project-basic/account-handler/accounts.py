from user import users


class account:
    savings = "savings account"
    salary = "salary account"
    def accounts(self):
       pass

    def account_type(self):               
    #AttributeError: 'function' object has no attribute 'user'
    #AttributeError: 'account' object has no attribute 'user'          
        pass                               
        
    
acc_type = account()
#acc_type.account_type()
print(acc_type.salary)