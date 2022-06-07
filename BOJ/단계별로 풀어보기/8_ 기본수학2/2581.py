import math

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

m = int(input())
n = int(input())

data = [i for i in range(m, n + 1)]
result = []
for x in data:
    if is_prime(x):
        result.append(x)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))