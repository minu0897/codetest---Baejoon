x = int(input())
y = int(input())

tmp1 = x//100

tmp = x//100 *100
x = tmp //y*y
if x//100 == tmp1:
    print(str(x%100).zfill(2))
else:
    print(str((x+y)%100).zfill(2))