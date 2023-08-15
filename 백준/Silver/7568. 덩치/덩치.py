n = int(input())
lis = []

for _ in range(n):
    tmp = list(map(int,input().split()))
    lis.append(tmp)

for a,b in lis:
    cnt=0
    for x,y in lis:
        if a<x and b<y:
            cnt+=1
    print(cnt+1,end=' ')