num=5
for line in range(1,num+1):
    for sp in range(line-1):
        print('  ',end=' ')
    for col in range(num-line+1):
        print(line,end=' ')
    print()
