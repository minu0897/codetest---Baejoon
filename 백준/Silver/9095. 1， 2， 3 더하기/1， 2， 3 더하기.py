n=int(input())
lis=[1,2,4]
for i in range(n):
    x=int(input())
    if x<len(lis):
        print(lis[x-1])
    else:
        for j in range(len(lis),x):
            lis.append(lis[j-1]+lis[j-2]+lis[j-3])
        print(lis[x-1])