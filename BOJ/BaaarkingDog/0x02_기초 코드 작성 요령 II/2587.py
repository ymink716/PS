# 대표값2
# https://www.acmicpc.net/problem/2587

array = []
for _ in range(5):
    array.append(int(input()))

array.sort()

print(sum(array) // 5)
print(array[2])