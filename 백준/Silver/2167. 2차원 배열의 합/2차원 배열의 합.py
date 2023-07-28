x,y = map(int, input().split())
list1 = []
list_sum = []
for i in range(x):
    tmp = list(map(int, input().split()))
    list1.append(tmp)
    for idx,j in enumerate(tmp):
        if idx == 0:
            list_sum.append(list())
            list_sum[i].append(j)
        else :
            list_sum[i].append(j+list_sum[i][idx-1])
n = int(input())
for i in range(n):
    a,b,c,d = map(int, input().split())
    #1,1,2,3
    value=0
    for row in range(a-1,c):
        value += list_sum[row][d-1]

        if b > 1:
            value -= list_sum[row][b-2]
    print(value)