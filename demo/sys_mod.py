# import sys
#
# print(sys.path)
# print(sys.argv)


import os

# 执行命令，但是不保存结果，cmd_res的值为是否执行成功
# cmd_res = os.system("dir")
cmd_res = os.popen("dir").read();
print(cmd_res);