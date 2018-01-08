s = "你好"
print(s.encode(encoding='gbk'))
print(s.encode(encoding='utf-8'))

import sys
print(sys.getdefaultencoding())