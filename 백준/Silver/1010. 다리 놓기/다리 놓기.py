cnt = int(input())

#dp : dp table 30x30 matrix 
#index : [0][*] [*][0] => not use
dp =[[0]*31 for _ in range(31)]

for j in range(30):
    dp[1][j+1] = j+1
    dp[j+1][j+1] = 1

def dpFun(row,col):
    if dp[row][col] == 0:
        dp[row][col] = int(dpFun(row,col-1)*col)//(col-row)
    
    return dp[row][col]


for i in range(cnt):
    n,m = map(int,input().split())
    n,m = min(n,m),max(n,m)

    print(dpFun(n,m))

