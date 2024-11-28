num=5
for line in range(num,0,-1):
    for sp in range(num-line):
        print('  ',end=' ')
    for col in range(line):
        print(line,end=' ')
    print()
