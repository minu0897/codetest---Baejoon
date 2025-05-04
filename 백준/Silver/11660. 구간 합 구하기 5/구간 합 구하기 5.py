n,m=map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]
dp_table =[[0]*n for _ in range(n)]

pos_s =  [list(map(int,input().split())) for _ in range(m)]


def dpFun(row,col):
    dp_table[row][col] = arr[row][col]
    nRow = row-1
    nCol = col-1
    if nRow>=0:
        dp_table[row][col] += dp_table[nRow][col]

    if nCol>=0:
        dp_table[row][col] += dp_table[row][nCol]

    if nRow>= 0 and nCol>=0:
        dp_table[row][col] -= dp_table[nRow][nCol]

for row in range(n):
    for col in range(n):
        dpFun(row,col)
        
for pos in pos_s:
    x1=pos[0]-1
    y1=pos[1]-1
    x2=pos[2]-1
    y2=pos[3]-1

    if (x1,y1)==(x2,y2):
        print(arr[x1][y1])
    else:
        result = dp_table[x2][y2]
        
        if y1-1>=0:
            result -= dp_table[x2][y1-1]
        if x1-1>=0:
            result -= dp_table[x1-1][y2]

        if x1-1>=0 and y1-1>=0:
            result += dp_table[x1-1][y1-1]
        print(result)