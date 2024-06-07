import math

n = int(input())
array = sorted([int(input()) for _ in range(n)])

gcd = array[1] - array[0]
for i in range(2, len(array)):
    gcd = math.gcd(array[i] - array[i - 1], gcd)

result = set()
for i in range(2, int(math.sqrt(gcd)) + 1):
    if gcd % i == 0:
        result.add(i)
        result.add(gcd // i)
result.add(gcd)

result = sorted(list(result))
for n in result:
    print(n, end=" ")

