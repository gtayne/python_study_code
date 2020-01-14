'''创建
def filterchar(string):
    "功能：过滤字符"
    import re
    pattern = r'(黑客)|(木马)|(nmsl)'
    sub = re.sub(pattern,'**',string)
    print(sub)
a = input('insert string')
filterchar(a)
'''
'''星期
def function_tips():
    import datetime
    mon = [ "今天星期一: \n",
        "今天星期二:\n",
        "今天星期三:\n",
       "今天星期四: \n",
       "今天星期五: \n",
       "今天星期六: \n",
       "今天星期日: \n"]
    day = datetime.datetime.now().weekday()
    print(mon[day])
function_tips()
'''
'''
def switchformat():
    d = int(input('please input a number'))
    print('b is Binary\no is Octal\nh is Hexadecimal\n')
    s = input('input a format you want to swith')
    if s is 'b':
        print('{:#b}'.format(d))
    elif s is 'o':
        print('{:#o}'.format(d))
    elif s is 'h':
        print('{:#x}'.format(d))
    else:
        print('please input a char between b/o/h')
switchformat()
'''
print("原值")

