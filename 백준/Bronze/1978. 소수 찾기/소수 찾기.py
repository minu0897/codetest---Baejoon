x = int(input())
arr = map(int,input().split())
cnt = 0

for i in arr:
    tmp1 = i
    y=2
    while y < tmp1:
        if i % y == 0:
            break
        y+=1
    if y == tmp1:
        cnt+=1
        
print(cnt)