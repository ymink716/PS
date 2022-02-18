import math

max_value = 10000
array = [True for _ in range(max_value + 1)]

for i in range(2, int(math.sqrt(max_value)) + 1):
    if array[i]:
        j = 2
        while i * j <= max_value:
            array[i * j] = False
            j += 1

for _ in range(int(input())):
    n = int(input())
    for i in range(n // 2, 1, -1):
        if array[i] and array[n - i]:
            print(i, n - i)
            break