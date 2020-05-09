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


def t2():
    try:
        d2 = DistributedDict('127.0.0.1', 5254)
    #try:
        #print('t2_1 D1',d1['GOOG'])
        print('t2_1 D2',d1['GOOG'])

    except:
        #transaction.abort()
        print('t2 error')

i1=Thread(target=t1)
i2=Thread(target=t2)
i1.start()
i2.start()

#transaction.commit()
#transaction.commit()



