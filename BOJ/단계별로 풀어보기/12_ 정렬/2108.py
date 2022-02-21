import sys
from collections import Counter

n = int(sys.stdin.readline())

data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))
data.sort()

print(round(sum(data) / n))
print(data[round(n // 2)])
c = Counter(data).most_common(2)
if len(c) == 2 and c[0][1] == c[1][1]:
    print(c[1][0])
else:
    print(c[0][0])
print(data[-1] - data[0])