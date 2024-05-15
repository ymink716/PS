a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

def f(n):
    return a1 * n + a0

def g(n):
    return n

# 계수 and 초기값 비교
if c >= a1 and f(n0) <= c * g(n0):
    print(1)
else:
    print(0)