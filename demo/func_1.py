
def func1(x,y):
    print(x,y)

func1(x=1,y=2)
# 关键参数不能位置参数的前面
# func1(x=3,4)

# 接受n个位置参数 转换为元祖
def func2(*args):
    print(args)

func2(2,3,4,'figal')

# 接受N个关键参数 转换为字典
def func3(**kwargs):
    print(kwargs)
func3(name='gao',age=19,sex='male')


