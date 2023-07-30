# X보다 작은 수
# https://www.acmicpc.net/problem/10871

n, x = map(int, input().split())
data = list(map(int, input().split()))

for i in data:
    if i < x:
        print(i, end=" ")