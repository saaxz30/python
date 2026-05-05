class users:

    def __init__(self):
        self.user_list = []

    def add_user(self,*name):
        for n in name:
            self.user_list.append(n)
        print(self.user_list)
        
    def get_user(self,name):
        if name in self.user_list:
            print("user available")
            return name
        else:
            return print(f"User Not Found : {name} in list")
        
    def delete_user(self,name):
        if name in self.user_list:
            self.user_list.remove(name)
            print(f"user : {name} deleted successfully, List after:{self.user_list}")
        else:
            return print(f"User Not Found : {name} in list")
if __name__ == "__main__":
    name = input("Enter the name (space separated) :").split()
    users_instance = users()
    users_instance.add_user(*name)
    users_instance.delete_user('sara')
    users_instance.get_user('nive')
