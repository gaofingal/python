
import time


def timer(func):
    def warpper(*args,**kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print("this is function run time is %s" %(stop_time-start_time))
    return warpper


@timer
def func1():
    time.sleep(1)
    print("this is decorate")


func1()