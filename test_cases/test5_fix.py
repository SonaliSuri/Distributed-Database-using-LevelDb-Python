from raft.client import DistributedDict
import transaction
from threading import Thread
from threading import Lock
from random import random
import time
d=DistributedDict('127.0.0.1',5254)
d['CRT']=1000
def t1():
    lock1=Lock()
    lock1.acquire()
    try:
        
        d1 = DistributedDict('127.0.0.1', 5254)
        d1['CRT'] = 100000
        time.sleep(1*1)
        print('Write by t1 D1 of ',d1['MNG'])

    except:
        #transaction.abort()
        print('t1 error')

    lock1.release()
def t2():
    lock2=Lock()
    lock2.acquire()
    try:
        d2 = DistributedDict('127.0.0.1', 5254)
        d2['CRT']= d2['CRT']+1200
        time.sleep(1*1)
        print('After write of 1200 to t2 D2',d2['MNG'])
        #print(d2)
    except:
        #transaction.abort()
        print('t2 error')
    lock2.release()

def t3():
    lock3=Lock()
    lock3.acquire()
    try:
        d3 = DistributedDict('127.0.0.1', 5254)
        print('Read of t3 D3',d3['CRT'])
        #print(d2)
    except:
        #transaction.abort()
        print('t3 error')
    lock3.release()


#l1=Lock()
#l1.acquire()
i1=Thread(target=t1)
i1.start()

time.sleep(3*1)
#l1.release()
#l1.acquire()
i2=Thread(target=t2)
i2.start()
#l1.release()

time.sleep(3*1)
i3=Thread(target=t3)
i3.start()
#transaction.commit()
#transaction.commit()
i1.join()
i2.join()
i3.join()

