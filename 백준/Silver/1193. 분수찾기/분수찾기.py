import math

n=int(input())

x,y=int(math.ceil((math.sqrt(1+8*n)-1)/2)),1

index=1
temp = True
t=4

for i in range(x-1):
    if temp:
        index +=1
    else:
        index +=t
        t+=4
    temp = not temp

if index>n:
    x-=(index - n)
    y+=(index - n)
else:
    x-=(n-index)
    y+=(n-index)

print(y,'/',x,sep="")