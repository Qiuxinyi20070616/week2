def add(a,b):
    return a+b
def jian(a,b):
    return a-b
def cheng(a,b):
    return a*b
def chu(a,b):
    return a/b
a=input('请输入你想做的运算：')
b=int(input('请输入第一个数：'))
c=int(input('请输入第二个数：'))
if a=='加':
    d=add(b,c)
elif a=='减':
    d=jian(b,c)
elif a=='乘':
    d=cheng(b,c)
else:
    d=chu(b,c)
print(f'运算结果为{d}')