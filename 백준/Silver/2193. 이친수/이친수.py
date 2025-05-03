n = int(input())

cnt_one = 0
cnt_ten = 1

for i in range(n-1):
    cnt_one,cnt_ten = cnt_one+cnt_ten,cnt_one

print(cnt_one+cnt_ten)