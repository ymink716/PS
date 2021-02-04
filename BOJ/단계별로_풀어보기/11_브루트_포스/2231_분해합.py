n = int(input())

answer = 0
for i in range(1, 1000001):
    result = i
    for s in str(i):
        result += int(s)
    if result == n:
        answer = i
        break

print(answer)