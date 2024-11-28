num=5
space=0
for line in  range(num*2,0,-2):
    for sp in range(space):
        print('  ',end=' ')
    for val in range(1,line):
        print(val,end=' ')
    print()
    space+=1
