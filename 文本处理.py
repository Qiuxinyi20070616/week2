with open("text3.txt","r",encoding="utf-8") as f:
    text=f.read()
words=text.split()
count={}
for word in words:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
result=sorted(count.items(),key=lambda x:x[1],reverse=True)
print("前10个高频词：")
for i in result[:10]:
    print(i)