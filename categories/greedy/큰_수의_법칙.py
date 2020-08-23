# N, M, K 입력 받기
n, m, k = map(int, input().split())
# N개의 수 입력 받기
data = list(map(int, input().split()))

data.sort()  # 정렬
first, second = data[-1], data[-2]  # 가장 큰 수와 두번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = m // (k+1) * k  # 반복하는 만큼
count += m % (k+1)  # k+1 로 나누어 떨어지지 않은 부분

result = 0
result += count * first  # 가장 큰 수 더하기
result += (m - count) * second  # 두 번째로 큰 수 더하기

print(result)