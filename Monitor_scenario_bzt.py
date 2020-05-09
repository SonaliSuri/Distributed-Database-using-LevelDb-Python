from raft.client import DistributedDict
import transaction
from threading import Thread
from collections import defaultdict
stock=input('Enter the stock which price is required :')
d=DistributedDict('127.0.0.1',5255)
d['KL']=1000
def byzantine_1():
    try:
        d1 = DistributedDict('127.0.0.1', 5254)
#        print('Server 1',d1)
        #d1['KL']=1000
        byz1=d1[stock]
        #print('t1 D1',d1['GOOG'])
        #transaction.commit()
        return byz1
    except:
        #transaction.abort()
        byz1=500
        print('t1 error')
        return byz1

def byzantine_2():
    try:
        d2=DistributedDict('127.0.0.1',5255)
 #       print('Server 2',d2)
        #d2['KL']=1000
        byz2=d2[stock]
        return byz2
    except:
        #return 0
        print('t2 error')
        return 500


def byzantine_3():
    try:
        d3= DistributedDict('127.0.0.1',5256)
  #      print('Server 3',d3)
        byz3=d3[stock]-500
        return byz3
    except:
      
        print('t3 error')
        return 500


val_1 = byzantine_1()
val_2 = byzantine_2()
val_3 = byzantine_3()

print('Value from Server 1',val_1)
print('Value from Server 2',val_2)
print('Value from Server 3',val_3)

map_dict=defaultdict(int)

map_dict[val_1]+=1
map_dict[val_2]+=1
map_dict[val_3]+=1
correct_key=-99
correct_val=-99
for (k,v) in sorted(map_dict.items(),key=lambda x:(-x[1],x[0])):
    correct_key=k
    correct_val=v
   
    #print('Correct value is ',k)
    break;


if correct_key!=val_1:
    print('Receiving incorrect value from Server 1')
elif correct_key!=val_2:
    print('Receiving incorrect value from Server 2')
else:
    print('Receiving incorrect value from Server 3')


    #print('Correct value is ',k)
    #break;

print('Correct Value',correct_key)


