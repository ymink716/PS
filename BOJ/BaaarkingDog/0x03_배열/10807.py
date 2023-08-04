# 개수 세기
# https://www.acmicpc.net/problem/10807

from collections import Counter

n = int(input())
array = list(map(int, input().split()))
v = int(input())

c = Counter(array)

print(c[v])