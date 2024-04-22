n, k = map(int, input().split())
array = list(map(int, input().split()))

if k == 1:
    print(max(array))
    exit()

if k == n:
    print(sum(array))
    exit()

left, right = 0, k
answer = sum(array[:k])

now = answer
while n > right:
    now -= array[left]
    now += array[right]

    if now > answer:
        answer = now

    left += 1
    right += 1

print(answer)