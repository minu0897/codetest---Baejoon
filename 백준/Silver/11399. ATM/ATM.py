n=int(input())
arr=list(map(int,input().split()))
arr.sort()
result=0
for i in arr:
    result += i*n
    n-=1
print(result)