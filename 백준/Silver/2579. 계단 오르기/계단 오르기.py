import sys

input = sys.stdin.readline

n = int(input())
score = [int(input()) for _ in range(n)]

if n == 1:
    print(score[0])
    exit()
elif n == 2:
    print(score[0] + score[1])
    exit()

dp = [0] * n

# 초기 계단 설정
dp[0] = score[0]
dp[1] = score[0] + score[1]
dp[2] = max(score[0] + score[2], score[1] + score[2])

# 점화식
for i in range(3, n):
    dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])

print(dp[-1])
