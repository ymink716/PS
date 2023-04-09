# 비밀번호 찾기

n, m = map(int, input().split())
d = dict()

for _ in range(n):
    site, password = input().split()
    d[site] = password

for _ in range(m):
    print(d[input()])
