str1 = "千山鸟飞绝"
str2 = "万径人踪灭"
str3 = "孤舟蓑笠翁"
str4 = "独钓寒江雪"
list1 = [list(str1),list(str2),list(str3),list(str4)]
print(list1)
for i in range(4):   ###列
    for j in range(5):   ###行
        if j == 4:
            print(list1[i][j])
        else:
            print(list1[i][j],end="")
