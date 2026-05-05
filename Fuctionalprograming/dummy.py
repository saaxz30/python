# n = 0 # UnboundLocalError: cannot access local variable 'n' 
# where it is not associated with a value
def Validation():
    n=0
    #globals()['n'] = 0
    valid_code = 0000
    entered_code = int(input('enter ur code :'))
    if valid_code == entered_code:
        print('Validation done')
    elif n <= 3:    
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

#Validation()

def opt_valid():
    valid_pin = 0000
    # correct_pin = ''
    attempts = 3
    for i in range(attempts):
        correct_pin = int(input('Enter the correct pin :'))
        if correct_pin == valid_pin:
            print('Validation done')
            return
        else:
            print('Wrong pin')
    print('You are out of max limit :3')
# opt_valid()
def kargs_(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
#kargs_( name = 'sara',age = 34)
num = 5
def ToCheckUnbound():
    if num > 1:
        mulOf5 = int(input("Enter an number to * with 5 :"))
        print(num*mulOf5)
#ToCheckUnbound()   
'''
dictn = {'devops':['linux','jenkins','aws','docker','git','scripting'],'development':('java','python','Node.js','.net')}
print(dictn['devops'][0][0:3])

full_name = 'saravanan deivasigamani'
initial = ''.join([word[0].upper() for word in full_name.split()])
print(initial)
exmp = ("sara","van","an")
joined = "".join(exmp)
print(joined) '''

def factorial(n):
    # init = n*(n-1) #56
    result = 1

    for x in range(n,0,-1):
        result = result * x
       
    print(result)
# factorial(4)
nums = [2,9,7,3]
target = 12
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j] == target:
            print([i,j])

def facByrecursion(nums):
    if nums == 1:
        return 1
    return nums * facByrecursion(nums-1)
print(facByrecursion(5))

"""def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
        
twoSum([1,3,5,8],8)   """     