def ret_num(ind):
    ret = 1
    for i in range(ind-1):
        ret*=10
        ret+=1
    return ret

def ret_num2(z,y):
    return z* y//10

def ret_num3(in_num,tmp,lst):
    j = (in_num%tmp)//(tmp//10)
    for i in range(j+1):
        if i == j:
            lst[i] += (in_num%(tmp//10))+1
        else :
            lst[i] += tmp//10

    
x = int(input())

# size = 천의 자리 수  -> 4
size = len(str(x))-1
num = 10**(size)
lst = [0 for _ in range(10)]

tmp = num
for i in range(size):
    ret_num3(x,tmp,lst)
    tmp //=10


#1
lst[x//num] += x%num+1

#2
i = 1
while i < x//num:
    lst[i] += num
    i+=1

#3
for i in range(10):
    in_data = ret_num2(size,num)
    if i==0 and size != 0:
        in_data -= ret_num(size)
    lst[i] += in_data

    tmp = num
    tmp1 = size
    tmpnum = x
    while tmp >= 10:
        if tmp ==num:
            in_data = ret_num2(tmp*tmp1,(tmpnum//tmp)-1)
        else:
            in_data = ret_num2(tmp*tmp1,(tmpnum//tmp))
        tmpnum%=tmp
        tmp//=10
        tmp1-=1
        lst[i] += in_data

#4

for i in lst:
    print(i,end=" ")