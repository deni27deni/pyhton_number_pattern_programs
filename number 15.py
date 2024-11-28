num=5
for line in range(1,num+1):
    for sp in range(num-line):
        print('  ',end=' ')
    for val in range(1,line+1):
        print(val,end=' ')
    print()
