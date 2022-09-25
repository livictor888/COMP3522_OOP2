#time since epoch
import time
#
# product = 1
# start_time = time.time()
#
# for i in range(1,40000):
#     product = product * i
#
# end_time = time.time()
# print('The result is %s digits long' % (len(str(product))))
# print('Took %s seconds to calculate.' % (end_time - start_time))


# #sleep test
# print(time.time())
#
# for i in range(3):
#     print('Tick')
#     time.sleep(1)
#     print(time.time())
#     print('Tock')
#     time.sleep(1)
#     print(time.time())

#
# #Specific time
# print (time.time())
# print(datetime.datetime.fromtimestamp(1000000))
# print(datetime.datetime.fromtimestamp(time.time()))

import datetime
#comparing times
a = datetime.datetime(2018,10,31,10,10,10)
halloween = datetime.datetime(2018, 10, 31)
nyd = datetime.datetime(2022, 1, 1)
delta = nyd - halloween
print('delta:', delta)

#timedelta example
delta2 = datetime.timedelta(days = 5, minutes = 11, seconds = 7)
print('seconds:', delta2)