import time


# 返回处理器时间，3,3废弃，改成time.process_time()测量运算时间，不包括sleep时间，不稳定，mac上测试不出来
print(time.clock())

# 计算与utc时间的时间差，以秒计算
print(time.altzone)

# Convert a time tuple to a string 返回时间格式"Fri Aug 19 11:14:16 2016",
print(time.asctime())

# 返回本地时间的struct time 时间对象格式
print(time.localtime())

# Convert a time in seconds since the Epoch to a string in local time.
# This is equivalent to asctime(localtime(seconds)). When the time tuple is
# not present, current time as returned by localtime() is used.
print(time.ctime())

# 日期字符串 转成  时间戳
string_2_struct = time.strptime("2016/05/22","%Y/%m/%d") #将 日期字符串 转成 struct时间对象格式
print(string_2_struct)
# #
struct_2_stamp = time.mktime(string_2_struct) #将struct时间对象转成时间戳
print(struct_2_stamp)



# 将时间戳转为字符串格式
print(time.gmtime(time.time()))
print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())) #将struct time格式的时间转化为时间戳



