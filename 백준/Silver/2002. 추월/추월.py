import sys


a = []
b = []

n = int(input())

for i in range(n):
    a.append(sys.stdin.readline())
for i in range(n):
    b.append(sys.stdin.readline())

cnt = 0

while len(a) !=0 :
    val = a[0]
    if val in b :
        for i in range(b.index(val) ):
            cnt+=1
            b.pop(0)
        b.pop(0)
    a.pop(0)

print(cnt)
