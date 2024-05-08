amount = int(input())

result = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    result += (a * b)

if amount == result:
    print('Yes')
else:
    print('No')