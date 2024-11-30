hr,min = map(int,input().split())

if(min >= 45):
    min = min-45
else :
    min = min-45
    hr -=1
    if hr < 0 :
        hr = 24 + hr
if min < 0:
    min += 60
print(hr,min)