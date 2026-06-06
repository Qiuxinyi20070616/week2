import random
a=random.randint(1,100)
while 1:
    b=int(input('请输入你猜测的数字：'))
    if b>a:
        print('这个数字大了')
    elif b<a:
        print('这个数字小了')
    else:
        print('猜对了！')
        break