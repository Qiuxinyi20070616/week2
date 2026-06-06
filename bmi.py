a=float(input('请输入身高(单位：m):'))
b=float(input('请输入体重(单位：kg):'))
BMI=b/a/a
print(f'你的BMI指数为{round(BMI,2)}')
if BMI<18.5:
    print('偏瘦')
elif BMI<=23.9:
    print('正常')
elif BMI<=27.9:
    print('超重')
else:
    print('肥胖')