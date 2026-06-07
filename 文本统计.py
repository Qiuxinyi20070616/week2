with open("text1.txt",'r',encoding="utf-8") as f:
    text=f.read()
print("字数为：",len(text))
lines=text.split('\n')
print("行数为：",len(lines))
longest=max(lines,key=len)
print ("最长行是：",longest)
print("本行长度为：",len(longest))