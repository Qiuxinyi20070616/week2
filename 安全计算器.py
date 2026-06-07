def add(a,b):
    return a+b
def jian(a,b):
    return a-b
def cheng(a,b):
    return a*b
def chu(a,b):
    return a/b
try:
    a=input('请输入你想做的运算：')
    b=int(input('请输入第一个数：'))
    c=int(input('请输入第二个数：'))
    if a=='加':
        d=add(b,c)
    elif a=='减':
        d=jian(b,c)
    elif a=='乘':
        d=cheng(b,c)
    elif a=='除':
        d=chu(b,c)
    else:
        print('输入的运算错误')
        exit()
    print(f'运算结果为{d}')
except ValueError:
    print('请输入正确数字')
except ZeroDivisionError:
    print('除数不能为0')