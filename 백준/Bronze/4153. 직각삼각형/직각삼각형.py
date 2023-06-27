while 1:
    x,y,z = map(int,input().split())
    if x==0 and y==0 and z==0 :
        break

    x **=2
    y **=2
    z **=2
    new = x+y+z - max(x,y,z)

    if max(x,y,z) == new:
        print('right')
    else:
        print('wrong')