n, k = map(int, input().split())
result = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # n이 k보다 작으면 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

# 남은 숫자 1씩 빼기
result += (n - 1)
print(result)