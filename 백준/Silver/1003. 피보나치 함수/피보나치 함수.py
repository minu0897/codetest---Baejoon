def fi(n,list,zero,one):
    if n ==0:
        zero[n]=1
        return 0
    if n ==1:
        one[n]=1
        return 1
    if list[n] != 0 :
        return list[n]
    else :
        list[n] = fi(n-1,list,zero,one) + fi(n-2,list,zero,one)
        zero[n] = zero[n-1] + zero[n-2]
        one[n] = one[n-1] + one[n-2]
        return list[n]

n = int(input())
list= [0 for _ in range(41)]
zero=[0 for _ in range(41)]
one=[0 for _ in range(41)]
for i in range(n):
    x= int(input())
    fi(x,list,zero,one)
    print(zero[x],one[x],sep=' ')