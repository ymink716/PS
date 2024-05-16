import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d1, d2 = dict(), dict()

for i in range(1, n + 1):
    p = input().rstrip()
    d1[i] = p
    d2[p] = i

for _ in range(m):
    s = input().rstrip()
    if s.isalpha():
        print(d2[s])
    else:
        print(d1[int(s)])
