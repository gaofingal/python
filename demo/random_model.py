import random

print(random.random())

#random.randint()的函数原型为：random.randint(a, b)，用于生成一个指定范围内的整数。
# 其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
print(random.randint(1,5))

#random.randrange的函数原型为：random.randrange([start], stop[, step])，
# 从指定范围内，按指定基数递增的集合中 获取一个随机数。如：random.randrange(10, 100, 2)，
# 结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。
# random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效。
print(random.randrange(1,10))


print(random.choice("fingal"))
#random.choice从序列中获取一个随机元素。
# 其函数原型为：random.choice(sequence)。参数sequence表示一个有序类型。
# 这里要说明一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。
# list, tuple, 字符串都属于sequence。有关sequence可以查看python手册数据模型这一章。
# 下面是使用choice的一些例子：
print(random.choice("学习Python"))#学
print(random.choice(["JGood","is","a","handsome","boy"]))  #List
print(random.choice(("Tuple","List","Dict")))   #List
print(random.sample([1,2,3,4,5],3))    #[1, 2, 5]
#random.sample的函数原型为：random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。

