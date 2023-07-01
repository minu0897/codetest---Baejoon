#5 21
#5 6 7 8 9
import sys
n,num = map(int,input().split())
tmp = sys.stdin.readline()

lis = list(map(int,tmp.split()))

lis.sort(key=lambda x:x)

max = 1
flag = False
for i in range(n-2):
    if flag:
        break
    x=i
    for j in range(n-x-1):
        if flag:
            break
        y = x+1+j
        for k in range(n-y-1):
            z = y+k+1
            if (lis[x]+lis[y]+lis[z]) < num and max < (lis[x]+lis[y]+lis[z]):
                max = (lis[x]+lis[y]+lis[z])
            if (lis[x]+lis[y]+lis[z]) == num :
                max = (lis[x]+lis[y]+lis[z])
                flag=True
                break
print(max)