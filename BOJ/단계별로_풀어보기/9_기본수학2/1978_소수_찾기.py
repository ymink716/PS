import math

n = int(input())
data = list(map(int, input().split()))

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

count = 0
for x in data:
    if is_prime(x):
        count += 1

print(count)