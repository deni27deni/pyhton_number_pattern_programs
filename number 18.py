num=5
r=num*2
for line in  range(1,num+1):
    for sp in range(line-1):
        print('  ',end=' ')
    for val in range(1,r):
        print(val,end=' ')
    print()
    r-=2
