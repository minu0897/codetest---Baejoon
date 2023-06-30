import sys
x = int(input())
lis=[]
for i in range(x):
    data = sys.stdin.readline().split()
    data.append(i)
    lis.append(data)
lis.sort(key = lambda x:(int(x[0]),x[2]))

for i in lis:
    print(i[0],i[1],sep=' ')