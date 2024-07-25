import sys
n = int(input())

cnt = 0

for _ in range(n):
    str = sys.stdin.readline()
    lis = []
    for s in str:
        if s == '\n':
            break
        elif lis and lis[-1] == s :
            lis.pop()
        elif lis and lis[-1] != s :
            lis.append(s)
        elif not lis:
            lis.append(s)
        else:
            break
    if len(lis) == 0:
        cnt += 1
print(cnt)