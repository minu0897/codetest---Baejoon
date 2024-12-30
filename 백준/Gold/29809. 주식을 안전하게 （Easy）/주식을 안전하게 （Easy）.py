p,c,k =map(int,input().split())
lis=list(map(int,input().split()))
D=[lis[0]]

for i in range(1,p):
    D.append(lis[i]-lis[i-1])

i=0
num=0
for i in range(1,p):
    num-=(c**i)*D[-i]
D.append(abs(num)%1000000007)

i=0
for i in range(p+1,k+1):
    D.append(abs((c**p)*D[i-p])%1000000007)
print(abs(D[-1])%1000000007)