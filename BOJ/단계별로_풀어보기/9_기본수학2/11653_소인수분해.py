n = int(input())

if n == 1:
    exit()

result = []
for i in range(2, n // 2 + 1):
    while n % i == 0:
        n = n // i
        result.append(i)
    if n == 1:
        break

if len(result) == 0:
    print(n)
else:
    for x in result:
        print(x)