x, y = map(int, input().split())

lis = [list(map(int, input())) for _ in range(x)]
max = 1
gap=1

while gap<min(x,y):
    nx = 0
    ny = 0
    while True:
        if lis[nx][ny] == lis[nx+gap][ny] and lis[nx][ny] == lis[nx][ny+gap]and lis[nx][ny] == lis[nx+gap][ny+gap]:
            max = gap+1
            break
        ny+=1
        if ny+gap >= y:
            nx+=1
            ny=0
        
        if nx+gap >= x:
            break
    gap+=1
print(max*max)