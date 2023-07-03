x,sum = map(int,input().split())
list = []

for i in range(x):
    list.append(int(input()))

tmp=x-1
cnt=0
while sum !=0:
    idx=tmp
    while sum < list[idx]:
        idx-=1
    cnt+=sum//list[idx]
    sum -=list[idx] * (sum//list[idx])
    tmp = idx -1

print(cnt)