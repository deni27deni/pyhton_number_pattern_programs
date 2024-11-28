num=5
space=num//2
star=1
for  line in range(num):
    for sp in range(space):
        print(' ',end=' ')
    for st in range(star,0,-1):
        print(st,end=' ')
    print()
    if num//2 >line:
        space-=1
        star+=2
    else:
        space+=1
        star-=2
    
