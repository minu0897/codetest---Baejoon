import sys 
N, M, B = map(int,input().split())
lis = []
dict = {}

for _ in range(N):
    str = sys.stdin.readline()
    for i in list(map(int,str.split())):
        if i in dict :
            dict[i] += 1
        else:
            dict[i] = 1
Sdict = sorted(dict.items(),reverse=True)

max = Sdict[0][0]
min = Sdict[-1][0]
minT=-1
minH=-1

for i in range(min,max+1):# i는 1씩 증가하는 수 비교되는 수
    Arr = lis
    bag = B
    TF = False
    off = False
    time = 0
    for num in Sdict:
        if num[0] > i:
            bag += num[1]*(num[0] - i)
            time += num[1]*(num[0] - i)*2
        elif num[0] < i:
            bag += num[1]*(num[0] - i)
            time -= num[1]*(num[0] - i)
            if bag < 0:
                off = True
                break
    if not off : 
        if minT == -1:
            minT = time
            minH = i
        elif minT > time:
            minT = time
            minH = i
        elif minT == time:
            if minH < i:
                minH = i

    


print(minT,minH,end=' ')