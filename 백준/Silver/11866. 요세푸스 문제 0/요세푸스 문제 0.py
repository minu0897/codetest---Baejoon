import collections as deque

dq = deque.deque()

x,y = map(int,input().split())

for i in range(x):
    dq.append(i+1)

print('<',end='')
tmp =''
while len(dq) !=0:
    for i in range(y-1):
        num = dq.popleft()
        dq.append(num)
    tmp += str(dq.popleft())+', ' 
print(tmp[:len(tmp)-2],end='>')