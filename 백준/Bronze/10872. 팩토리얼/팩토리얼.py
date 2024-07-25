n = int(input())

if n==1 or n==0:
    print(1)
else:
    result = 1
    while n >= 2:
        result *= n
        n -= 1
    print(result)