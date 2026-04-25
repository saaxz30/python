n = 0
def Validation():
    n=0
    valid_code = 0000
    entered_code = int(input('enter ur code :'))
    if valid_code == entered_code:
        print('Validation done')
    elif n<3:    
        if valid_code != entered_code:
            print("'please enter valid code'")
            while n < 2:
                retry = int(input("enter correct code :"))
                if n < 1 and retry != valid_code:
                    print("'Please enter valid code'")    
                elif n == 1 and retry != valid_code:
                    print("Wrong code,you are out of max limit:3") 
                    break
                elif retry == valid_code:
                    print("Validation done")
                    break
                n += 1   
Validation()