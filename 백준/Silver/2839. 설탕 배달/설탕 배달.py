x = int(input())
if x%5==0:
    print(x//5)
else:
    cnt=0
    bol = False
    while x > 0:
        cnt+=1
        x -= 3
        if x%5==0 and x > 0:
            print(cnt+(x//5))
            bol = True
            break
    if not bol:
        if x==0:
            print(cnt)
        else:
            print(-1)
        