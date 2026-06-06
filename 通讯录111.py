txl={}
name=input('请输入联系人姓名：')
phone=input('请输入联系人电话：')
txl[name]=phone
a=input('请输入要查找的联系人姓名：')
if a in txl:
    print(f'这位联系人的电话是：{txl[a]}')
else:
    print('该位联系人不存在')
b=input('请输入要删去的联系人姓名：')
if b in txl:
    del txl[b]
else:
    print('该位联系人不存在')