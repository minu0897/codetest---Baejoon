import sys

def search(num,lst):
    flag=False
    sidx=0
    eidx=len(lst)-1

    if lst[sidx] <= num and lst[eidx] >= num:
        while sidx != eidx and not flag:
            if sidx == eidx-1:
                break
            midx = (eidx + sidx) //2
            if lst[sidx] == num or lst[eidx] == num:
                flag=True
                print(1)
                break
            elif lst[midx] ==num:
                flag=True
                print(1)
                break
            elif lst[midx] > num:
                eidx = midx
            else :
                sidx = midx

        if not flag:
            print(0)
    else:
        print(0)

#4 5 6
#0 1 2 

x= int(input())
tmp = sys.stdin.readline()
lst1 = list(map(int,tmp.split()))
lst1.sort(key=lambda x:x)

y= int(input())
tmp = sys.stdin.readline()
lst2 = list(map(int,tmp.split()))
for i in lst2:
    search(i,lst1)