import time
from raft.client import DistributedDict
d = DistributedDict('127.0.0.1', 5255)

#SET operation run
sum_insert = 0
total_op = 100
for x in range(1, total_op):
  print(x)
  start_time = time.time()
  d[x] = 100000
  print("Insert--- %s seconds ---" % (time.time() - start_time))
  sum_insert = sum_insert + (time.time() - start_time)

print(sum_insert)
avg = sum_insert / total_op
print('avg', avg)

time.sleep(3)
#GET operation run
sum_get = 0
for x in range(1, total_op):
  print(x)
  start_time = time.time()
  print(d[x])
  print("Get--- %s seconds ---" % (time.time() - start_time))
  sum_get = sum_get + (time.time() - start_time)

print(sum_get)
avg = sum_get / total_op
print('avg', avg)

#del operation run
sum_del = 0
for x in range(1, total_op):
  print(x)
  start_time = time.time()
  del d[x]
  print("Del--- %s seconds ---" % (time.time() - start_time))
  sum_del = sum_del + (time.time() - start_time)

print(sum_del)
avg = sum_del / total_op
print('avg', avg)

# time.sleep(1)
#
# start_time = time.time()
# print(d['keynew1'])
# print("Get--- %s seconds ---" % (time.time() - start_time))
#
# start_time = time.time()
# del d['keynew1']
# print("Del--- %s seconds ---" % (time.time() - start_time))
#
# start_time = time.time()
# d['keynew2'] = 200000
# print("Insert--- %s seconds ---" % (time.time() - start_time))
#
# time.sleep(1)
#
# start_time = time.time()
# print(d['keynew2'])
# print("Get--- %s seconds ---" % (time.time() - start_time))
#
# start_time = time.time()
# d['keynew3'] = 300000
# print("Insert--- %s seconds ---" % (time.time() - start_time))
# time.sleep(1)
#
# start_time = time.time()
# print(d['keynew3'])
# print("Get--- %s seconds ---" % (time.time() - start_time))
#
# start_time = time.time()
# del d['keynew3']
# print("Del--- %s seconds ---" % (time.time() - start_time))
#
# start_time = time.time()
# d['keynew4'] = 400000
# print("Insert--- %s seconds ---" % (time.time() - start_time))
# time.sleep(1)
#
# start_time = time.time()
# print(d['keynew4'])
# print("Get--- %s seconds ---" % (time.time() - start_time))
#
#
# start_time = time.time()
# del d['keynew4']
# print("Del--- %s seconds ---" % (time.time() - start_time))

