num=5
for line in range(num,0,-1):
    for sp in range(line-1,0,-1):
        print('  ',end=' ')
    for val in range(num,line-1,-1):
        print(val,end=' ')
    print()
