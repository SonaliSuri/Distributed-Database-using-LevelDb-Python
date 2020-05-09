from raft.client import DistributedDict
import transaction
from threading import Thread
d=DistributedDict('127.0.0.1',5254)
d['OPT']=1000

def t1():
    try:
        
        d1 = DistributedDict('127.0.0.1', 5254)
        d1['OPT'] = 2000
        print('Write of t1 D1',d1['OPT'])
        #transaction.commit()
    except:
        #transaction.abort()
        print('t1 error')

def t2():

    try:
        d2 = DistributedDict('127.0.0.1', 5254)
        d2['OPT'] =d2['OPT']+1200
        print('Write of 1200 by t2 D2',d2['OPT'])
        #transaction.commit()
    except:
        transaction.abort()
        print('t2 error')

def t3():
    
    try:
        d3 = DistributedDict('127.0.0.1', 5254)
        d3['OPT'] =d3['OPT']+500
        print('Write of 500 t3 D3',d3['OPT'])
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



