from collections import deque

n, k = map(int, input().split())

numbers = deque([i for i in range(1, n + 1)])

print('<', end='')

while len(numbers) > 1:
    for j in range(k - 1):
        numbers.append(numbers.popleft())
    print(str(numbers.popleft()) + ',', end=' ')

print(str(numbers.popleft()) + '>')