n, m = map(int, input().split())

a, b = set(), set()

for _ in range(n):
    a.add(input())

for _ in range(m):
    b.add(input())

result = a & b

print(len(result))
for p in sorted(result):
    print(p)