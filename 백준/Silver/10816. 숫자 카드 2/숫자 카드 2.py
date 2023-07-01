import sys

n = int(input())
data =sys.stdin.readline().split()

count ={}

for i in data:
    if count.get(i) == None:
        count[i] = 1
    else:
        count[i] = count[i]+1

n = int(input())
data =sys.stdin.readline().split()

for i in data:
    if count.get(i) == None:
        print(0,end=' ')
    else:
        print(count.get(i),end=' ')