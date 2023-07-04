prtcnt = 0
num = 1
n = int(input())
while prtcnt != n:
    num +=1
    numt = num

    cnt=0
    #6이 3개있는지 체크
    while numt != 0:
        tt = numt%10
        numt//=10
        if tt == 6:
            cnt+=1
        else:
            cnt =0

        if cnt==3:
            prtcnt+=1
            break
print(num)