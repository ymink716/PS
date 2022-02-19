import math

max_value = 246912
array = [True for _ in range(max_value + 1)]
for i in range(2, int(math.sqrt(max_value)) + 1):
    if array[i]:
        j = 2
        while i * j <= max_value:
            array[i * j] = False
            j += 1

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for check in array[n + 1:2 * n + 1]:
        if check:
            count += 1
    print(count)