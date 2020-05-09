from raft.client import DistributedDict
import transaction
from threading import Thread
d=DistributedDict('127.0.0.1',5254)
d['GOOG']=0
def t1():
    try:
        d1 = DistributedDict('127.0.0.1', 5254)
        d1['GOOG'] = 100000
        print('t1 D1',d1['GOOG'])
        #transaction.commit()
    except:
        #transaction.abort()
        print('t1 error')

    try:
        d1['GOOG']=d1['GOOG']+300
        print('t1_1 D1',d1['GOOG'])
        #print('t1_1 D2',d2['GOOG'])
    except:
        #transaction.abort()
        print('t1_1 error')


def t2():
    try:
        d2 = DistributedDict('127.0.0.1', 5254)
        d2['GOOG'] =500
        print('t2 D2',d2['GOOG'])
        transaction.commit()
    except:
        transaction.abort()
        print('t2 error')

    try:
        #print('t2_1 D1',d1['GOOG'])
        print('t2_1 D2',d2['GOOG'])

    except:
        #transaction.abort()
        print('t2_1 error')

i1=Thread(target=t1)
i2=Thread(target=t2)
i1.start()
i2.start()
i1.join()
i2.join()
#transaction.commit()
#transaction.commit()



