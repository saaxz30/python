'What is an thread?'
# Thread is an component of process which runs chuncks of the process simultaneously.
# 1 process may have multiple threads.
'How it can be craeted?'
# Either by classes or by function (pythonic way)
'Why do we need an thread?'
# To run desired process simultaneously
'How the thread works? in multiprocessing'
# Threads works with in the time space given to it and if it could'nt complete the whole process
# in time it will wait for its time again untill the process gets over(e.g:round robbin)
from threading import Thread
from time import sleep,time
'---------------class thread--------------------'
class counter(Thread):
    def run(self):
        for i in range(5,-1,-1):
            sleep(1)
            print("Tik Tik Tik",i) 
class Boom(Thread):
    def run(self):
        for i in range(5):
            sleep(1)
            print("Boom")

t1 = counter()
t2 = Boom()

t1.start()
t2.start()
'---------------function thread---------------'
def hello():
    i = 0
    while i <= 4:
        print('Hello')
        i += 1

def hi():
    j = 0
    while j <= 4:
        print('Hi')
        j += 1
t3 = Thread(target=hello)
t4 = Thread(target=hi)

t3.start()
t4.start()

t3.join()
t4.join()  # Join is for waiting till threads combine again so that it becomes single thread again.
print('Thanks')

def downloads(file):
    print('Downloading file...', file)
    sleep(0.5)
    print('Downloading completed')
files = ['sara.txt','nive.txt','image.jpeg']
threads = []
for f in files:
    t5 = Thread(target= downloads,args=(f,))
    threads.append(t5)
for t in threads:
    t.start()
'------------------------Multiprocessing------------------------------'
# Threads share the same memory inside the process and will have same GIL which
# locks the one thread at a time which is slow compared to separate,
# running simultaneously via multiprocessing and have separate GIL
from multiprocessing import Process
def P1():
    data = [23,67,89,40,35]
    for x in data:
        print(x)
def P2():
    package = [1,2,3,4,5,6,7,8]
    for x in package:
        print(x)

p1 = Process(target=P1)
p2 = Process(target=P2)
start = time()
p1.start()
p2.start()
end = time()
print(F"time taken :{end - start:.2f}")