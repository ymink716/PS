import math

m, n = map(int, input().split())
array = [True for i in range(n + 1)]
array[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for x in range(m, n + 1):
    if array[x]:
        print(x)