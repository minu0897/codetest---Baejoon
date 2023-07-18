import sys

n = int(input())
arr = []
sum = 0
for _ in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)
    sum += num
arr.sort()
print(round(sum/n))
print(arr[(n//2)])
#최빈값 구하기
max = None
max_cnt=0
prev=None
cnt = 0
maxarr = []
for i in arr:
    if prev == None:
        prev = i
        cnt = 1
        max_cnt=1
        maxarr.append(i)
    else:
        if prev == i :
            cnt+=1
        else:
            cnt = 1
            prev = i
        if cnt > max_cnt :
            max_cnt = cnt
            maxarr.clear()
            maxarr.append(i)
        elif cnt == max_cnt :
            maxarr.append(i)



if len(maxarr) > 1:
    print(maxarr[1])
else:
    print(maxarr[0])

print(arr[-1]-arr[0])