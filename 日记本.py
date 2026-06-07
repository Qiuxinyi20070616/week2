import datetime
text=input("请输入今天的日记：")
now = datetime.now()
time = now.strftime("%Y-%m-%d %H:%M:%S")
with open("diary.txt", "a", encoding="utf-8") as f:
    f.write(f"{time}\n")
    f.write(text+'\n')