import threading
from threading import *


def hello(name):
    for i in range(1, 25):
        print('hello:', name, i)


def hi(name):
    for i in range(1, 25):
        print('hi:', name, i)


t1 = threading.Thread(target=hello, args=('raj',))
t2 = threading.Thread(target=hi, args=('myname',))

t1.start()
t2.start()
