x,y = map(int,input().split())
list = [0 for _ in range(y+1)]
list[0] = -1
list[1] = -1
num=1
while num<=y:
    if num ==1 or list[num] == -1:
        num+=1
        continue
    tmp = 2
    if x <= num:
        print(num)
    while num*tmp <y+1:
        list[num*tmp] = -1
        tmp+=1
    num+=1