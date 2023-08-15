i=input()
str = input()
sumval = 0
tmp = 0
for i in str:
    sumval += (ord(i)-ord('a')+1)*(31**tmp)
    tmp+=1
print(sumval)