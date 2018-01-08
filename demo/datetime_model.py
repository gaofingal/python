import datetime
import time

# 2017-10-16 10:35:00.689382
print(datetime.datetime.now())

# 2017-10-16
print(datetime.date.fromtimestamp(time.time()))


# 2017-10-19 10:41:33.107493    now time = 2017-10-16 10:35:00.689382
print(datetime.datetime.now() + datetime.timedelta(3))
print(datetime.datetime.now() + datetime.timedelta(-3))
print(datetime.datetime.now() + datetime.timedelta(hours=3))
print(datetime.datetime.now() + datetime.timedelta(minutes=30))