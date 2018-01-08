

'''
r 表示只读
w 表示只写
a 表示追加，只读
'''
f = open("txt",'r',encoding="utf-8");

data = f.read()

print(data)

f.close()





print("--------------------------练习二-------------------------------")

f = open("txt",'r',encoding="utf-8");

data = f.readlines()

for index,lines in enumerate(data):
    if index == 9:
        print("-----这个是跳过的内容--------")
        continue
    print(lines.strip())

f.close()



print("-------------------------练习三------------------------------")
f = open("txt",'r',encoding="utf-8");
for line in f:
    print(line)
f.close()

print("-------------------------练习四------------------------------")
f = open("txt",'r',encoding="utf-8");
# 指针当前位置
f.tell()
# 到达那个位置
f.seek(10)
# 关闭文件句柄
f.close()


print("--------------------------练习五----------------------------------")
f = open('txt1','w+',encoding='utf-8')
f.write("this is first line \n")
f.write("this is first line \n")
f.write("this is first line \n")
f.write("this is first line \n")
print(f.tell())
f.seek(10)
print(f.tell())
print(f.readline())
f.write("this is second line \n")
f.seek(0)
data = f.read()
print(data)
f.close()

print("--------------------练习六-------------------------")
with open('txt1','r',encoding='utf-8') as f_read,\
open('txt2','w',encoding='utf-8') as f_write:
    for line in f_read:
        print(line)
        if line == 'this is second line':
            print("这两句是相等的")
            line.replace(line,"this is second copy")
        f_write.write(line);
