n =int(input())

x=1
cnt=1
while x<n:
  cnt+=1
  x+=cnt*2
  x+=(cnt-1)*2+(cnt-2)*2
print(cnt)
  