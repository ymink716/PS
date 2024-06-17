import math
import sys

input = sys.stdin.readline

MAX = 1000000
prime = [True for i in range(MAX + 1)]
prime[1] = False

for i in range(2, int(math.sqrt(MAX)) + 1):
    if prime[i] == True:
        j = 2
        while i * j <= MAX:
            prime[i * j] = False
            j += 1

for _ in range(int(input())):
    n = int(input())
    count = 0

    for i in range(2, n // 2 + 1):
        if prime[i] and prime[n - i]:
            count += 1

    print(count)