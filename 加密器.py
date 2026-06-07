with open("text4.txt","r",encoding="utf-8") as f:
    text=f.read()
newtext=""
for i in text:
    newtext+=chr(ord(i)+3)
with open("text5.txt","w",encoding="utf-8") as f:
    f.write(newtext)