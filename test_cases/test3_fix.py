from raft.client import DistributedDict
import transaction
from threading import Thread
from threading import Lock
from random import random
import time
d=DistributedDict('127.0.0.1',5254)
d['RKL']=1000
def t1():
    lock1=Lock()
    lock1.acquire()
    try:
        
        d1 = DistributedDict('127.0.0.1', 5254)
        #d1['GOOG'] = 100000
        #time.sleep(1*1)
        print('t1 D1',d1['RKL'])
    except:
        #transaction.abort()
        print('t1 error')

    lock1.release()
def t2():
    lock2=Lock()
    lock2.acquire()
    try:
        d2 = DistributedDict('127.0.0.1', 5254)
        print('t2 D2',d2['RKL'])
        #print(d2)
    except:
        #transaction.abort()
        print('t2 error')
    lock2.release()

#l1=Lock()
#l1.acquire()
i1=Thread(target=t1)
i1.start()

#time.sleep(5*1)
#l1.release()
#l1.acquire()
i2=Thread(target=t2)
i2.start()
#l1.release()

#transaction.commit()
#transaction.commit()
i1.join()
i2.join()

