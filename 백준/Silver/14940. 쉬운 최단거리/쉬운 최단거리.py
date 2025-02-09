import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
sX,sY=0,0
for t in arr:
    if 2 in t:
        sX = t.index(2)
        break
    sY+=1

que = deque()
que.append((sY,sX))
visit = set((sY,sX))
arr[sY][sX]=0

while que:
    temp=[[1,0],[-1,0],[0,1],[0,-1]]
    val = que.popleft()
    (tarY,tarX)=val
    for t in temp:
        x = tarX+t[0]
        y = tarY+t[1]
        if 0<=x<m and 0<=y<n:
            if (arr[y][x]== 1 and (y,x) not in visit) or ((y,x) in visit and arr[y][x]>arr[tarY][tarX]+1):
                que.append((y,x))
                arr[y][x] = arr[tarY][tarX]+1
                visit.add((y,x))


for i in range(n):
    for j in range(m):
        print( -1 if arr[i][j] == 1 and (i,j) not in visit else arr[i][j],end=" ")
    print()