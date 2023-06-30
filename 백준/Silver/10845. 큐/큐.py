import sys
from collections import deque
n = int(input())
que = deque()


for i in range(n):
    ins = sys.stdin.readline()
    me = list(map(str,ins.split()))
    if me[0] =='push':
        num = int(me[1])
        que.append(num)
    if me[0] =='pop':
        if len(que) == 0:
            sys.stdout.write('-1'+'\n')
        else:
            sys.stdout.write(str(que.popleft())+'\n')
    if me[0] =='size':
        sys.stdout.write(str(len(que))+'\n')
    if me[0] =='empty':
        if len(que) == 0:
            sys.stdout.write('1'+'\n')
        else:
            sys.stdout.write('0'+'\n')
    if me[0] =='front':
        if len(que) == 0:
            sys.stdout.write('-1'+'\n')
        else:
            num = que.popleft()
            
            sys.stdout.write(str(num)+'\n')
            que.appendleft(num)
    if me[0] =='back':
        if len(que) == 0:
            sys.stdout.write('-1'+'\n')
        else:
            num = que.pop()
            sys.stdout.write(str(num)+'\n')
            que.append(num)