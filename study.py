# commodity = [['T0001', '笔记本电脑'],
#              ['T0002', '华为荣耀6X'],
#              ['T0003', 'iPad'],
#              ['T0004', '华为荣耀V9'],
#              ['T0005', 'MacBock']]
# for i in range(5):   ###行
#     for j in range(2):   ###列
#         if j == 1 :
#             print("\t型号"  + commodity[i][j])
#         else:
#             print("编号" + commodity[i][j] ,end = "")
#print(commodity)
# print("编号" + commodity[0][0] + "\t型号" + commodity[0][1])
# print("编号" + commodity[1][0] + "\t型号" + commodity[1][1])1

list_seat = ['10-01','10-02','10-03','10-04']
print("座位有")
    for index,item in enumerate(list_seat):
        print(index+1,item)
    print("请输入要选择的座位")
    seat = int(input("请输入序号1-4中的一个"))
    if seat in range(5):
        print("您已经选择座位" + list_seat[seat+1])
    else:
        print("输入的序号有误")

