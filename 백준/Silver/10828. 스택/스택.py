import sys
x = int(input())

lis = []
for i in range(x):
    data = sys.stdin.readline().strip()
    da = data.split(' ')
    if da[0] == 'empty':
        if len(lis) != 0:
            print(0)
        else :
            print(1)
    elif da[0] == 'push':
        lis.append(int(da[1]))
    elif da[0] == 'pop':
        if len(lis)==0:
            print(-1)
        else:
            print(lis.pop())
    elif da[0] == 'size':
        print(len(lis))
    elif da[0] == 'top':
        if len(lis)==0:
            print(-1)
        else:
            print(lis[len(lis)-1])