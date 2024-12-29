n=int(input())
cnt=0

for i in range(n):
    num=i+1
    if num <100:
        cnt+=1
    else:
        snum = str(num)
        gap = int(snum[0])-int(snum[1])
        for j in range(len(snum)-1):
            if int(snum[j])-int(snum[j+1]) != gap:
                cnt-=1
                break
        cnt+=1
print(cnt)