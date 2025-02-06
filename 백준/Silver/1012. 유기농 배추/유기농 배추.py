import sys
from collections import deque

def Fbfs(m,n,items,pos):
    visited = set()
    que = deque()

    que.append(pos)
    
    while que:
        tar = que.popleft()
        y,x=tar
        if (y,x) not in visited:
            visited.add((y,x))
            items[y][x] = 2

            if y+1<n and items[y+1][x]==1:
                que.append((y+1,x))
            if y-1>=0 and items[y-1][x]==1:
                que.append((y-1,x))
                
            if x+1<m and items[y][x+1]==1:
                que.append((y,x+1))
            if x-1>=0 and items[y][x-1]==1:
                que.append((y,x-1))



input = sys.stdin.readline
t=int(input())
for _ in range(t):
    m,n,k = map(int,input().split())
    items = [[0]*m for _ in range(n)]

    for _ in range(k):
        x,y = map(int,input().split())
        items[y][x]=1

    result = 0
    for startX in range(m):
        for startY in range(n):
            if items[startY][startX] == 1:
                Fbfs(m,n,items,(startY,startX))
                result+=1
    print(result)