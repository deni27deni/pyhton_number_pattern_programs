num=5
space=num//2
star=1
for line in range(num):
    for sp in range(space):
        print('  ',end=' ')
    for val in range(1,star+1):
        print(val,end=' ')
    print()
    if num//2 >line:
        star+=1
        space-=1
    else:
        star-=1
        space+=1
