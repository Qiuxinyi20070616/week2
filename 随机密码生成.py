import random
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = ""
for i in range(8):
    password += random.choice(chars)
print("随机生成的密码为：", password)