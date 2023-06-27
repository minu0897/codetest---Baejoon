import sys

x=int(input())
cnt = [0 for _ in range(10001)]

for i in range(x):
    inda = int(sys.stdin.readline())
    cnt[inda-1] += 1

for i in range(10001):
    for j in range(cnt[i]):
        print(i+1)
        