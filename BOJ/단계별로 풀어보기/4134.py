import sys
import math

input = sys.stdin.readline

def is_prime_number(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())

    while True:
        if is_prime_number(n):
            print(n)
            break
        else:
            n += 1