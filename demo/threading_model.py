#
# import threading
# import time
#
#
# def sayhi(num):
#     print("running on number:%s" %num)
#     time.sleep(3)
#
# if __name__ == 'main':
#     t1 = threading.Thread(target=sayhi,args=(1,))
#     t2 = threading.Thread(target=sayhi,args=(2,))
#
#     t1.start()
#     t2.start()
#
#     print(t1.getName())
#     print(t2.getName())