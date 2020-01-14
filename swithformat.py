def switch_format(d):
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
while True:
    a = int(input('please insert a integer'))
    if int(a) != 0:
        switch_format(a)
        break
switch_format(a)




