import sys

lis = []
for _ in range(20):
    lis.append(0)

n = int(input())

for i in range(n):
    str = sys.stdin.readline()

    if str[0] =='a' and str[1] =='d':
        str,num = str.split()
        num=int(num)
        if lis[num-1]==0:
            lis[num-1]=1
    elif str[0]=='a' and str[1] =='l':
        for j in range(20):
            lis[j]=1
    elif str[0]=='r':
        str,num = str.split()
        num=int(num)
        if lis[num-1]==1:
            lis[num-1]=0
    elif str[0]=='c':
        str,num = str.split()
        num=int(num)
        print(lis[num-1])
    elif str[0]=='t':
        str,num = str.split()
        num=int(num)
        if lis[num-1]==0:
            lis[num-1]=1
        else:
            lis[num-1]=0
    elif str[0]=='e':
        for j in range(20):
            lis[j]=0
    