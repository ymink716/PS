import sys
input = sys.stdin.readline

n = int(input())

now = set()
for _ in range(n):
    p, r = input().split()

    if r == 'enter':
        now.add(p)
    if r == 'leave':
        now.remove(p)

now = sorted(now, reverse=True)

for p in now:
    print(p)