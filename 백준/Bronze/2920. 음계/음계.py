arr = [*map(int,input().split())]


gu1,gu2 = 0,0
for idx,val in enumerate(arr):
    if idx == 0 :
        value = val
    else:
        if value > val:
            gu1 = 1
        elif value < val :
            gu2 = 1
    value = val

if gu1 == 0:
    print('ascending')
elif gu2 == 0:
    print('descending')
else :
    print('mixed')