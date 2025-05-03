n,d = map(int,input().split())

#d = n이면 dp_table은 n+1이다.
dp_table=[0]
short = []
idx=0

for i in range(n):
    short.append(list(map(int,input().split())))

short = sorted(short, key=lambda x: x[1])
    
for i in range(1,d+1):
    n1 = dp_table[i-1]+1#지름길 없이 걷기
    temp = [n1]

    if idx < n and short[idx][1] == i:
        for j in range(idx,len(short)):
            if short[idx][1] == i:
                temp.append(dp_table[short[j][0]]+short[j][2])
                idx+=1
            else:
                break
        
    
    dp_table.append(min(temp))

print(dp_table[d])