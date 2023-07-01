import sys

n = int(input())
num=1
ptr = []
stck = []
flag = False
for i in range(n):
    data = int(sys.stdin.readline())
    while True:
        if num < data:
            stck.append(num)
            ptr.append('+')
            num += 1
        elif num == data:
            ptr.append('+')
            ptr.append('-')
            num += 1
            break
        elif num > data:
            ptr.append('-')
            if stck.pop() != data:
                flag = True
            break
    if flag:
        break
if flag:
    print('NO')
else :
    for i in ptr:
        print(i)