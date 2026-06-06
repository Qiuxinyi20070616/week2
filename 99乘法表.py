for a in range(1,10):
    for b in range(1,a+1):
        c=a*b
        if b!=a:
            print(f'{b}*{a}={c}',end=' ')
        else:
            print(f'{b}*{a}={c}\n')