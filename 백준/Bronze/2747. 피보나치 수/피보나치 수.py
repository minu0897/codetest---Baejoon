n=int(input())
item=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
if n<=17:
    print(item[n])
else:
    start = 18
    while start <= n:
        item.append(item[start-1]+item[start-2])
        start+=1
    print(item[n])