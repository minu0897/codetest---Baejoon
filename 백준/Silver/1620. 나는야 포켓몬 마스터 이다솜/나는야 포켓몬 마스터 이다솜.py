import sys

n, q = map(int, input().split())
lis=[input() for _ in range(n)]
dic={lis[i]:i+1 for i in range(n)}

for i in range(q):
    f = sys.stdin.readline().strip()

    if f[0]>='0' and f[0]<='9':#숫자
        sys.stdout.write(lis[int(f)-1]+'\n')
    else:
        sys.stdout.write(str(dic.get(f))+'\n')