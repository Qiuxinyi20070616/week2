text=input("请输入今天的日记：")
with open("diary.txt",'a',encoding="utf-8") as f:
    f.write(text+'\n')