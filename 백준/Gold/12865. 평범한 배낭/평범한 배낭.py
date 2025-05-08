n, k = map(int, input().split())
items = []
dp_table = [0] * (k + 1)

# 무게, 가치
for _ in range(n):
    items.append(list(map(int, input().split())))

for weight, value in items:
    for i in range(k, weight - 1, -1):  # 역방향으로!
        dp_table[i] = max(dp_table[i], dp_table[i - weight] + value)

print(max(dp_table))