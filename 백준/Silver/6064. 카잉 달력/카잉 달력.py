x = int(input())

for i in range(x):
    a,b,c,d = map(int,input().split())
    num = c
    if a==c:
        c=0
    if b==d:
        d=0
    while num <= a*b:
        if num%(b)==d:
            print(num)
            break
        else:
            num+=a
    if not(num%(a)==c and num%(b)==d):
        print(-1)