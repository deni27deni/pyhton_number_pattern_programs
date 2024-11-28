num=5
star=1
for line in range(num):
    for st in range(1,star+1):
        print(st,end=' ')
    print()
    if num//2 > line:
        star+=1
    else:
        star-=1
