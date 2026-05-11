'What is exception?'
# A critical case which need to be handled so that the code won't crash
'Why we need to handle them?'
# So that the app won't be crashed and the logic's after that code block will be executed
def connect(url:str,code:str):
    print(f'connecting to :{url}//{code}')

data = []
for i in range(0,3):
    try:
        name = input("enter your name :")
        age = int(input("enter your age :"))
    except Exception as e:
        print("please enter an integer :",e)
        dict = {name:age}
        data.append(dict)
        continue
    
print(data)
'Finally block'
try:
    connect('https//xyz.com',"200:ok")  #TypeError: connect() missing 1 required positional argument: 'code'
finally:
    print('connection closed successfully')
# Used to close resources even if the app crash it is safest way to close anything.
# Even if the code fails finally will be executed.