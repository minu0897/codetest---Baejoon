import sys
from collections import deque

input = sys.stdin.readline
x, y = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(y)]
que = deque()
visit = set()
size = 0  # 방문한 셀 개수

# 초기 상태 설정
for i in range(y):
    for j in range(x):
        if arr[i][j] == 1:
            que.append((i, j))
            visit.add((i, j))
            size += 1  # 익은 토마토 개수 증가
        elif arr[i][j] == -1:
            size += 1  # 빈 공간 개수 증가

size_arr = x * y
day = 0

# BFS 실행
while que:
    for _ in range(len(que)):  # 현재 큐에 있는 모든 노드 처리
        pY, pX = que.popleft()

        for dY, dX in [(0,1), (0,-1), (1,0), (-1,0)]:
            nY, nX = pY + dY, pX + dX
            if 0 <= nY < y and 0 <= nX < x and arr[nY][nX] == 0 and (nY, nX) not in visit:
                visit.add((nY, nX))  # 방문 체크
                que.append((nY, nX))  # BFS 큐에 추가
                arr[nY][nX] = 1  # 토마토 익음
                size += 1  # 익은 토마토 개수 증가
    
    if que:  # BFS가 진행 중이면 하루 증가
        day += 1

# 모든 토마토가 익었는지 확인
print(day if size == size_arr else -1)
