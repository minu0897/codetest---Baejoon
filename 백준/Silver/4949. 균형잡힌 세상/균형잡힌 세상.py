import sys


while True:
    x=sys.stdin.readline()
    lis = []
    ft = True
    end = False
    for idx,val in enumerate(x):
        if idx==0 and val=='.':
            end=True
            break
        if val in ('(',')','[',']'):
            if val in ('(','['):
                lis.append(val)
            elif val == ')':
                if len(lis) == 0:
                    print('no')
                    ft=False
                    break
                if lis.pop() != '(':
                    print('no')
                    ft=False
                    break
            elif val == ']':
                if len(lis) == 0:
                    print('no')
                    ft=False
                    break
                if lis.pop() != '[':
                    print('no')
                    ft=False
                    break
    if end:
        break
    if ft:
        if len(lis) != 0:
            print('no')
        else:
            print('yes')
        
