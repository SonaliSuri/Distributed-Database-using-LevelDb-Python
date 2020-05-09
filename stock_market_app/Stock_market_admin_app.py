from raft.client import DistributedDict
from threading import Thread
d=DistributedDict('127.0.0.1',5254)
def t1():
    try:
        stck=input('Enter the stock code ')
        price= int(input('Enter the stock price '))
        d1 = DistributedDict('127.0.0.1', 5254)
        d1[stck] = price
        print('Value inserted successfully into the database')
        #transaction.commit()
    except:
        #transaction.abort()
        print('t1 error')
#transaction.commit()
#transaction.commit()

t1()

