import sys

#O는 빈 공간, X는 벽, I는 도연이, P는 사람이다. I가 한 번만 주어짐이 보장된다.

#OOOPO
#OIOOX
#OOOXP

input = sys.stdin.readline

x,y = map(int,input().split())
items=[input()[0:y] for _ in range(x)]
pos_row=0
pos_col=0
result=0
visited=set()
stack=[]
for idx,item in enumerate(items):
    if 'I' in item:
        pos_row=idx
        pos_col=item.find('I')
        break

stack.append((pos_row,pos_col))

while stack:
    row,col = stack.pop()
    
    if (row,col) not in visited:
        if items[row][col]=='P':
            result+=1
        visited.add((row,col))

        if row+1 < x and items[row+1][col] !='X' and (row+1,col) not in visited:
            stack.append((row+1,col))
        if row-1 >= 0 and items[row-1][col] !='X' and (row-1,col) not in visited:
            stack.append((row-1,col))
        if col+1 < y and items[row][col+1] !='X' and (row,col+1) not in visited:
            stack.append((row,col+1))
        if col-1 >= 0 and items[row][col-1] !='X' and (row,col-1) not in visited:
            stack.append((row,col-1))
            
if result == 0:
    print('TT')
else:
    print(result)