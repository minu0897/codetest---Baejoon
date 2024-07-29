a = {}
input()

for i in list(map(int,input().split())):
    a[i] = 1

for i in list(map(int,input().split())):
    if i in a:
        a.pop(i)

if len(a) == 0:
    print(0)
    exit()
else:
    print(len(a))

for i in dict(sorted(a.items())):
    print(i,end=" ")