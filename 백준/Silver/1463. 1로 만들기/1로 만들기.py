x=int(input())

lis = [0,0,1,1]

for i in range(4,x+1):
    tmp = i
    cnt = 0
    t =[]
    
    t.append(lis[tmp-1])

    if tmp%2==0:
        t.append(lis[tmp//2 ]) 

    if tmp%3==0:
        t.append(lis[tmp//3 ]) 
    
    midx = min(t)

    lis.append(midx+1)

print(lis[x])