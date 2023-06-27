import sys
x=int(input())
lis = [0 for _ in range(2000001)]
for i in range(x):
    idx = int(sys.stdin.readline())+1000000
    lis[idx] += 1

for i in range(2000001):
    if lis[i] == 1:
        sys.stdout.write(str(i-1000000)+'\n')