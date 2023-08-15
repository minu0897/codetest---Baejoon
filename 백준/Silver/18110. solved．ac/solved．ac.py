import sys

def newRound(num,n=1):
    num *= 10**n

    if num%10>=5:
        return int(num // 10**n +1)
    else:
        return int(num // 10**n)


n = int(input())
lis = []
sum_val = 0
for _ in range(n):
    num = int(sys.stdin.readline())
    lis.append( num )
    sum_val+=num
lis.sort()

tmp = newRound(n*0.15)

for i in range(tmp):
    sum_val-=lis[i]
    sum_val-=lis[len(lis)-i-1]


if n == 0:
    print(0)
else:
    print(newRound(sum_val/(n-tmp-tmp)))