import sys
from collections import deque

input = sys.stdin.readline

def Fdfs(items,start):
    n=len(items)
    visited=set()
    stack =[start]

    while stack:
        num = stack.pop()

        if num not in visited:
            print(num+1,end=" ")
            visited.add(num)

            for idx,val in enumerate(reversed(items[num])):
                if val == 1 and n-idx-1 not in visited:
                    stack.append(n-idx-1)

def Fbfs(items,start):
    n=len(items)
    visited=set()
    que = deque([start])

    while que:
        num = que.popleft()

        if num not in visited:
            print(num+1,end=" ")
            visited.add(num)

            for idx,val in enumerate(items[num]):
                if val ==1 and idx not in visited:
                    que.append(idx)



n,m,v= map(int,input().split())

items=[[0]*n for _ in range(n)]

for _ in range(m):
    x,y = map(int,input().split())
    items[x-1][y-1] = 1
    items[y-1][x-1] = 1

Fdfs(items,v-1)
print()
Fbfs(items,v-1)