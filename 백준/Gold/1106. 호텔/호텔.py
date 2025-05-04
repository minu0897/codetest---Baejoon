target,n = map(int,input().split())
info = set()
dp_table = []
max = 0

for _ in range(n):
    t1,t2 = map(int,input().split())
    info.add((t1,t2))
    if max < t2:
        max = t2

for i in range(target+max):#비용/고객
    dp_table.append([-1,i])
dp_table[0][0]=0

for i in range(1,target+max):
    for data in info:
        if dp_table[i][1]-data[1] >=0  and dp_table[dp_table[i][1]-data[1]][0] != -1:
            if dp_table[i][0] == -1:
                dp_table[i][0] = dp_table[dp_table[i][1]-data[1]][0]+data[0]
            else:
                if dp_table[i][0] > dp_table[dp_table[i][1]-data[1]][0]+data[0]:
                    dp_table[i][0] = dp_table[dp_table[i][1]-data[1]][0]+data[0]

result=[]
for item in dp_table[(-1)*max:]:
    if item[0] != -1 :
        result.append(item)

print(min(result,key=lambda x:x[0])[0])