result = []
for _ in range(10):
    n = int(input()) % 42
    result.append(n)

result = set(result)
print(len(result))

