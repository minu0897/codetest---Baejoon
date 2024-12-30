import sys
input = sys.stdin.readline

n,m=map(int,input().split())
lis=list(map(int,input().split()))

for i in range(1,n):
    lis[i]=lis[i-1]+lis[i]
for _ in range(m):
    i,j=map(int,input().split())
    if i==j and i==1:
        print(lis[i-1])
    elif i==j:
        print(lis[j-1]-lis[j-2])
    elif i>1:
        print(lis[j-1]-lis[i-2])
    else:
        print(lis[j-1])