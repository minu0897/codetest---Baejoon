import sys
input=sys.stdin.readline

n=int(input())

for _ in range(n):
    temp_n=int(input())
    hash_lis={}
    for __ in range(temp_n):
        temp_s=input().split()
        temp_s=temp_s[1]
        if hash_lis.get(temp_s)==None:
            hash_lis[temp_s]=1
        else:
            hash_lis[temp_s]+=1
    num=1
    for i,val in enumerate(hash_lis):
        num*=hash_lis[val]+1
    print(num-1)