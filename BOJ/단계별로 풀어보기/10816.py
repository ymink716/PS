import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
c = Counter(map(int, input().split()))

m = int(input())
for p in map(int, input().split()):
    result = c.get(p)
    if result:
        print(result, end=" ")
    else:
        print(0, end=" ")