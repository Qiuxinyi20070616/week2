while True:
    print("1.添加账单")
    print("2.查看账单")
    print("3.统计账单")
    print("4.保存账单")
    choice=input("请输入功能：")
    if choice=="1":
        date=input("请输入日期：")
        kind=input("请输入类别：")
        money=input("请输入金额：")
        note=input("请输入备注：")
        try:
            money=float(money)
            if kind=="":
                print("类别不能为空")
            else:
                with open("账单.txt","a",encoding="utf-8") as f:
                    f.write(f"{date},{kind},{money},{note}\n")
        except ValueError:
            print("金额必须是数字")
    elif choice=="2":
        try:
            with open("账单.txt","r",encoding="utf-8") as f:
                text=f.read()
            print("账单内容：")
            print(text)
        except FileNotFoundError:
            print("还没有账单文件")
    elif choice=="3":
        total={}
        try:
            with open("账单.txt","r",encoding="utf-8") as f:
                lines=f.readlines()
            for line in lines:
                data=line.strip().split(",")
                kind=data[1]
                money=float(data[2])
                if kind in total:
                    total[kind]+=money
                else:
                    total[kind]=money
            print("统计结果：")
            for k,v in total.items():
                print(f"{k}:{v}")
        except FileNotFoundError:
            print("还没有账单文件")
    elif choice=="4":
        print("成功保存")
        break
    else:
        print("输入错误")