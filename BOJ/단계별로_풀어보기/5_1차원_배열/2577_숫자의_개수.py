a = int(input())
b = int(input())
c = int(input())

n = a * b * c
result = [0 for _ in range(10)]

for i in str(n):
    result[int(i)] += 1

for j in result:
    print(j)