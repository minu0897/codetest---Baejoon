n = int(input())
cnt=0
max = 0
num = n
max_num = 0
while num != 0:

    tmp1 = n
    tmp2 = num
    cnt=2
    while tmp1-tmp2 >= 0:
        cnt+=1
        tmp = tmp1 - tmp2
        tmp1 = tmp2
        tmp2 = tmp
    if max < cnt:
        max = cnt
        max_num = num
    num-=1
print(max)
print(n,end=' ')
f = n
e = max_num
while f-e >=0:
    print(e,end=' ')
    tmp = f
    f = e
    e = tmp -e
print(e,end=' ')