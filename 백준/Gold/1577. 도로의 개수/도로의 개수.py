n,m = map(int,input().split())
n+=1
m+=1
#dp_table : nxm matrix
dp_table=[[0]*m for _ in range(n)]
dp_table[0][0]=1

#못 가는 구역
no_cnt = int(input())
no_arr = set()

for i in range(no_cnt):
    x1,y1,x2,y2 = map(int,input().split())
    no_arr.add((x1,y1,x2,y2))
    no_arr.add((x2,y2,x1,y1))

for row in range(n):
    for col in range(m):
        if row==0 and col == 0:
            continue
        else:
            if col-1 < 0:
                bef_col = 0
            else:
                if (row,col-1,row,col) not in no_arr:
                    bef_col = dp_table[row][col-1]
                else:
                    bef_col=-1

            if row-1 < 0:
                bef_row = 0
            else:
                if (row-1,col,row,col) not in no_arr:
                    bef_row = dp_table[row-1][col]
                else:
                    bef_row=-1

            if bef_col == -1 and bef_row == -1:
                dp_table[row][col] = bef_row+bef_col+2
            elif bef_col == -1 or bef_row == -1:
                dp_table[row][col] = bef_row+bef_col+1
            else:
                dp_table[row][col] = bef_row+bef_col

if dp_table[n-1][m-1] == -1:
    print(0)
else:
    print(dp_table[n-1][m-1])