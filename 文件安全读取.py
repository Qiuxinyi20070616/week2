try:
    with open("test2.txt", "r", encoding="utf-8") as f:
        text = f.read()
    print("文件内容：")
    print(text)
except FileNotFoundError:
    print("文件不存在")
except UnicodeDecodeError:
    print("文件编码错误")