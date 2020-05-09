from raft.client import DistributedDict
import transaction
from threading import Thread
d=DistributedDict('127.0.0.1',5254)
d['MNG']=1000

def t1():
    try:
        
        d1 = DistributedDict('127.0.0.1', 5254)
        d1['MNG'] = 10000
        print('Write of t1 D1',d1['MNG'])
        #transaction.commit()
    except:
        #transaction.abort()
        print('t1 error')

def t2():

    try:
        d2 = DistributedDict('127.0.0.1', 5254)
        #d2['GOOG'] =500
        print('Read by t2 D2',d2['MNG'])
        #transaction.commit()
    except:
        transaction.abort()
        print('t2 error')

def t3():
    
    try:
        d3 = DistributedDict('127.0.0.1', 5254)
        #d2['GOOG'] =500
        print('Read of t3 D3',d3['MNG'])
        #transaction.commit()
    except:
        transaction.abort()
        print('t3 error')

i1=Thread(target=t1)
i2=Thread(target=t2)
i3=Thread(target=t3)
i1.start()
i2.start()
i3.start()

#transaction.commit()
#transaction.commit()



