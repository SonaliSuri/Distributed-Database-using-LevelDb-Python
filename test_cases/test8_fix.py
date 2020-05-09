from raft.client import DistributedDict
import transaction
from threading import Thread
from threading import Lock
from random import random
import time
d=DistributedDict('127.0.0.1',5254)
d['STX']=0
d['STC']=0
def t1():
    lock1=Lock()
    lock1.acquire()
    try:
        
        d1 = DistributedDict('127.0.0.1', 5254)
        d1['STX'] =100000
        time.sleep(1*1)
        print('Transaction t1 after the write of 100000 : New value',d1['STX'])
        time.sleep(1*1)
        #transaction.commit()
        #d1['GOOG']=1200
        time.sleep(1*1)
        d1['STC']=6000
        time.sleep(1*1)
        print('Transaction t1 after setting the value of the stock STC to 6000 : New value',d1['STC'])
        time.sleep(1*1)
        d1['STX']=d1['STX']-5000
        print('Transaction t1 after decrementing the STX stock value by 5000', d1['STX']
                )
        time.sleep(1*1)
        d1['STC']=d1['STC']+5000
        time.sleep(1*1)
        print('Transaction t2 after incrementing the value of stock STC by 5000' , d1['STC'])

    except:
        #transaction.abort()
        print('t1_1 error')

    lock1.release()
def t2():
    lock2=Lock()
    lock2.acquire()
    try:
        d2 = DistributedDict('127.0.0.1', 5254)
        d2['STC'] =d2['STC']+500
        time.sleep(1*1)
        print('Transaction t2 after incrementing the value of STC by 500 : ',d2['STC'])
        #transaction.commit()
        #print('t2_1 D1',d1['GOOG'])
        time.sleep(1*1)
        #print('Read the final value of the stock GOOG : ',d2['MTX'])
        d2['STX'] = d2['STX']+2400
        print('Transaction t2 after incrementing the value of stock STX by 2400', d2['STX'])
    except:
        #transaction.abort()
        print('t2_1 error')
    lock2.release()

#l1=Lock()
#l1.acquire()
i1=Thread(target=t1)
i1.start()

time.sleep(5*1)
#l1.release()
#l1.acquire()
i2=Thread(target=t2)
i2.start()
#l1.release()

#transaction.commit()
#transaction.commit()
i1.join()
i2.join()

