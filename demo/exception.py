
class myexception(Exception):
    def __init__(self,msg):
        self.mssage = msg
    # def __str__(self):
    #     return "自定义的异常"



try:
    raise myexception("这是我的异常")
except Exception as e:
    print(e)