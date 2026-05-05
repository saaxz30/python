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
        continue
    dict = {name:age}
    data.append(dict)
print(data)

try:
    connect('https//xyz.com')
finally:
    print('connection closed successfully')

'Finally block'
# Used to close resources even if the app crash it is safest way to close anything.
