num=5
star=num
for line in range(num):
    for val in range(star,num+1):
        print(val,end=' ')
    print()
    if num//2 >line:
        star-=1
    else:
        star+=1
