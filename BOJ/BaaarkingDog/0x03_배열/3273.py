# 두 수의 합
# https://www.acmicpc.net/problem/3273

n = int(input())
array = list(map(int, input().split()))
x = int(input())

array.sort()
left, right = 0, n - 1
answer = 0

while left < right:
    now = array[left] + array[right]

    if now < x:
        left += 1
        continue
    elif now == x:
        answer += 1

    right -= 1

print(answer)