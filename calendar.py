import datetime
time = datetime.datetime.now().weekday()
print(time)
blank = [' ',' ',' ',' ',' ',' ']
week = ['一','二','三','四','五','六','日']
for a in range(1,13):
    mouthes = []
    mouthes.append(a)
    yue = ['月份']
    month = [mouthes + yue + blank]
    days = [day for day in range(1,32)]
    print(month,"\n",week)
    print(days[0:7])
    print(days[7:14])
    print(days[14:21])
    print(days[21:28])
    print(days[28:])
    #for day in range(1,32):
    #    days = []
    #    days.append(day)
    #for index,item in enumerate(days):
    #    if index <= 7:
    #        print(item,'\n')
            #continue
    #    elif index <= 14:
    #        print(item,'\n')
    #        #continue
    #    elif index <= 21:
    #        print(item,'\n')
    #    else:
    #        print(item,'\n')
