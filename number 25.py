num=5
star=num
for line in range(num):
    for st in range(num,star-1,-1):
        print(st,end=' ')
    print()
    if num//2 > line:
        star-=1
    else:
        star+=1
