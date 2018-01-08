product_list = [
    ('mac',10000),
    ('iphone',5000),
    ('pen',100),
    ('pant',170),
    ('thinkPad',7000),
]

shop_list = []

# 输入工资总数
salary = input(">>>输入你的工资：")
if salary.isdigit():
    salary = int(salary)
else:
    print("不要闹你输入的不是钱")

while True:
    # 讲商品循环出来
    for k,v in enumerate(product_list):
        print(k,':',v)
    choice_item = input(">>>选择商品：");
    if choice_item.isdigit():
        # 转化为整数
        choice_item = int(choice_item)
        if choice_item > len(product_list) and choice_item < -1:
            print("商品不存在")
        else:
            salary -= product_list[choice_item][1]
            if salary < 0:
                print("余额：%s，余额不足" %(salary))
                continue;
            print("购买成功,余额%s" %(salary))
            shop_list.append(product_list[choice_item])
            for item in shop_list:
                print(item)
        print("输入正确")
    else:
        print("非法输入")
