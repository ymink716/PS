# 최댓값
# https://www.acmicpc.net/problem/2562

max_value = 0
index = 0
for i in range(1, 10):
    n = int(input())
    if n > max_value:
        max_value = n
        index = i

print(max_value)
print(index)