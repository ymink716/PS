import sys

n = int(input())
data = [0 for _ in range(10001)]

for _ in range(n):
    num = int(sys.stdin.readline())
    data[num] += 1

for i in range(len(data)):
    for _ in range(data[i]):
        print(i)