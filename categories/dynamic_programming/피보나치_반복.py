d = [0] * 100  # dp 테이블 초기화
d[1], d[2] = 1, 1  # 첫 번째와 두 번째 피보나치 수는 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])