import sys


n=int(sys.stdin.readline())
x=int(sys.stdin.readline())

cnt=0

lis=[[0]*n for _ in range(n)]
vis=[0]*n

def fun_cnt(idx):
    global lis
    global vis
    global cnt
    if vis[idx-1]==0:
        vis[idx-1]=1
        if idx!=1:
            cnt+=1
    for i,v in enumerate(lis[idx-1]):
        if v==1 and vis[i]==0:
            fun_cnt(i+1)

for i in range(x):
    a,b=map(int,sys.stdin.readline().split())
    lis[a-1][b-1]=1
    lis[b-1][a-1]=1

fun_cnt(1)

print(cnt)