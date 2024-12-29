n=int(input())
lis=[]
for i in range(n):
    lis.append(input())
i=0
for i in range(len(lis[0])):
    v = True
    for j in range(n):
        if lis[0][i] != lis[j][i]:
            v=False
            break
    if v:
        print(lis[0][i],end="")
    else:
        print("?",end="")
