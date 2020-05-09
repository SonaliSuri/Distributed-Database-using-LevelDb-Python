from raft.client import DistributedDict
import transaction
from threading import Thread
d=DistributedDict('127.0.0.1',5254)
d['GOOG']=0
d['MTX']=0
def t1():
    try:
        d1 = DistributedDict('127.0.0.1', 5254)
        d1['GOOG'] = 100000
        print('Transaction t1 after the write of 100000 : New value',d1['GOOG'])
        #transaction.commit()
    except:
        #transaction.abort()
        print('t1 error')

    try:
        d1['GOOG']=1200
        d1['MTX']=2000
        print('Transaction t1 after setting MTX : New value',d1['MTX'])
        #print('t1_1 D2',d2['GOOG'])
    except:
        #transaction.abort()
        print('t1_1 error')


def t2():
    try:
        d2 = DistributedDict('127.0.0.1', 5254)
        d2['GOOG'] =d2['GOOG']+500
        print('Transaction t2 after setting the value of the stock to 500 : New value',d2['GOOG'])
        transaction.commit()
    except:
        transaction.abort()
        print('t2 error')

    try:
        #print('t2_1 D1',d1['GOOG'])
        d2['MTX'] = d2['MTX'] + 2400
        print('Transaction t2 Read the value of the stock MTX : ',d2['MTX'])

    except:
        #transaction.abort()
        print('t2_1 error')

i1=Thread(target=t1)
i2=Thread(target=t2)
i1.start()
i2.start()

#transaction.commit()
#transaction.commit()



