from raft.client import DistributedDict
import transaction
from threading import Thread
d=DistributedDict('127.0.0.1',5254)
d['STX']=0
d['STC']=0
def t1():
    try:
        d1 = DistributedDict('127.0.0.1', 5254)
        d1['STX'] = 100000
        d1['STC']=6000
        print('Transaction t1 after the write of 100000 to STX : New value',d1['STX'])
        print('Transaction t1 after the write of 6000 to STC',d1['STC'])
        #transaction.commit()
    except:
        #transaction.abort()
        print('t1 error')

    try:
        d1['STX']=d1['STX']-5000
        #d1['MTX']=2000
        print('Transaction t1 after setting STX : New value',d1['STX'])
        #print('t1_1 D2',d2['GOOG'])
    except:
        #transaction.abort()
        print('t1_1 error')

    try:
        d1['STC']=d1['STC']+500
        print('Transaction t1 after setting STC : New value',d1['STC'])
        #print('t1_1 D2',d2['GOOG'])
    except:
        #transaction.abort()
        print('t1_1 error')


def t2():
    try:
        d2 = DistributedDict('127.0.0.1', 5254)
        d2['STC'] =d2['STC']+500
        print('Transaction t2 after updating the value of the stock STC by 500 : New value',d2['STC'])
        transaction.commit()
    except:
        transaction.abort()
        print('t2 error')

    try:
        #print('t2_1 D1',d1['GOOG'])
        d2['STX'] = d2['STX'] + 400
        print('Transaction t2 updates the value of the stock STX by 400 : ',d2['MTX'])
       
    except:
        #transaction.abort()
        print('t2_1 error')



def t3():
    try:
        d3 = DistributedDict('127.0.0.1', 5254)
        d3['STC'] =d3['STC']-1000
        print('Transaction t3 after updating the value of the stock STC by 500 : New value',d3['STC'])
        d3['STX']=d3['STX']+200
        transaction.commit()
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



