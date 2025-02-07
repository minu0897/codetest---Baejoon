import sys
from collections import deque

input = sys.stdin.readline
x,y = map(int,input().split())
size_arr = x*y
size=0
arr=[list(map(int,input().split())) for _ in range(y)]
visit = set()
result = 0
que = deque()
for i in range(y):
    for j in range(x):
        if arr[i][j] == 1:
            que.append((i,j))
            size+=1
        elif arr[i][j] == -1:
            size+=1



day = 0

while que:
    temp_size = len(que)

    for _ in range(temp_size):
        qItem=que.popleft()
        pY,pX=qItem
        if pX+1 < x and arr[pY][pX+1]==0 and (pY,pX+1) not in visit:
            que.append((pY,pX+1))
            visit.add((pY,pX+1))
            arr[pY][pX+1] = 1
            size+=1
            
        if pX-1 >= 0 and arr[pY][pX-1]==0 and (pY,pX-1) not in visit:
            que.append((pY,pX-1))
            visit.add((pY,pX-1))
            arr[pY][pX-1] = 1
            size+=1
            
        if pY+1 < y and arr[pY+1][pX]==0 and (pY+1,pX) not in visit:
            que.append((pY+1,pX))
            visit.add((pY+1,pX))
            arr[pY+1][pX] = 1
            size+=1
            
        if pY-1 >= 0 and arr[pY-1][pX]==0 and (pY-1,pX) not in visit:
            que.append((pY-1,pX))
            visit.add((pY-1,pX))
            arr[pY-1][pX] = 1
            size+=1
        

        #print('----------------')
        #for i in range(y):
        #    for j in range(x):
        #        print('%2d'%arr[i][j],end=" ")
        #    print()
        #print('-----',day,'--------')
                    
    day+=1


if size_arr==size:
    print(day-1)
else:
    print(-1)