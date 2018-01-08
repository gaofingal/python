
list_1= [1,2,3,3,2,1]

list_2 = set(list_1)

list_3 = {3,4,5}

print(list_2)

# 交集
print(list_3.intersection(list_2))
# 并集
print(list_2.union(list_3))
# 差集
print(list_3.difference(list_2))
# 子集 和 父集
print(list_3.issubset(list_2))
print(list_3.issuperset(list_2))
# 反向差集
print(list_3.symmetric_difference(list_2))
# 判断两个集合是否有交集
print(list_3.isdisjoint(list_2))


print("----------------------------------------")


list_4 = {9,7,6}

list_4.add(0)

if 8 in list_4:
    print("在里面呢")
else:
    print("不在里面")

print(list_4)