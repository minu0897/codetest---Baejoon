import sys
input=sys.stdin.readline

n=int(input())
size =int(input())
tar="I"
for i in range(n):
    tar+="OI"

Str=input()

idx=0
cnt=0
while True:
    Str = Str[idx:]
    fIdx = Str.find(tar)

    if fIdx ==-1:
        break
    else:
        cnt+=1
        idx = fIdx+1

print(cnt)