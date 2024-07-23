#cursor를 기준으로 left right 스택을 정의한다.
import sys

l = list(sys.stdin.readline())
l.pop()
r = []

for i in range(int(input())):
    instr = sys.stdin.readline()

    if instr[0] == 'L' and l:
        r.append(l.pop())
    elif instr[0] == 'D' and r:
        l.append(r.pop())
    elif instr[0] == 'B' and l:
        l.pop()
    elif instr[0] == 'P':
        l.append(instr[-2])
        


for i in l:
    print(i,end="")

for i in r[::-1]:
    print(i, end="")