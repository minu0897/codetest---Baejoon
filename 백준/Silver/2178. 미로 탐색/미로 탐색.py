import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
items = [list(map(int, input()[0:-1])) for _ in range(n)]

visited = set()
que = deque()

que.append((0,0))

while que:
    target = que.popleft()
    row,col = target
    if target not in visited:
        visited.add(target)

        if row+1<n and items[row+1][col] > 0:
            if (row+1,col) not in visited:
                items[row+1][col] = items[row][col]+1
                que.append((row+1,col))
            elif (row+1,col) in visited and items[row+1][col] > items[row][col]+1 and (row+1,col)!=(0,0):
                items[row+1][col] = items[row][col]+1

        if row-1>=0 and items[row-1][col] > 0:
            if (row-1,col) not in visited:
                items[row-1][col] = items[row][col]+1
                que.append((row-1,col))
            elif (row-1,col) in visited and items[row-1][col] > items[row][col]+1 and (row-1,col)!=(0,0):
                items[row-1][col] = items[row][col]+1

        if col+1<m and items[row][col+1] > 0:
            if (row,col+1) not in visited:
                items[row][col+1] = items[row][col]+1
                que.append((row,col+1))
            elif (row,col+1) in visited and items[row][col+1] > items[row][col]+1 and (row,col+1)!=(0,0):
                items[row][col+1] = items[row][col]+1

        if col-1>=0 and items[row][col-1] > 0:
            if (row,col-1) not in visited:
                items[row][col-1] = items[row][col]+1
                que.append((row,col-1))
            elif (row,col-1) in visited and items[row][col-1] > items[row][col]+1 and (row,col-1)!=(0,0):
                items[row][col-1] = items[row][col]+1
    

print(items[n-1][m-1])