import time

def consumer(name):
    while True:
        num = yield
        print("第[%s]个包子,[%s]要开始吃包子了" %(num,name))

def productor(name):
    a = consumer('A')
    b = consumer('B')

    next(a)
    next(b)

    print("[%s]开始做包子" %name)
    for i in range(10):
        time.sleep(1)
        print("做了一个包子")
        a.send(i)
        b.send(i)


productor("Gao")
