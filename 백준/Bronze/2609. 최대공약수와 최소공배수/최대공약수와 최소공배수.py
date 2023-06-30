def retList(num,mn):
    lis=[0 for _ in range(mn)]
    tmp=2
    while num != 1:
        while num %tmp == 0:
            lis[tmp-1]+=1
            num //=tmp
        tmp+=1

    return lis


x,y = map(int,input().split())
lis1=retList(x,max(x,y))
lis2=retList(y,max(x,y))

tmp1 = 1
tmp2 = 1
for i in range(max(x,y)):
    if lis1[i]>0 and lis2[i]>0:
        tmp1 *=((i+1)**min(lis1[i],lis2[i]))
    if lis1[i]>0 or lis2[i]>0:
        tmp2 *=((i+1)**max(lis1[i],lis2[i]))
print(tmp1,tmp2,sep='\n')