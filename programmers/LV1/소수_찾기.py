# 소수 찾기 (못품)
def solution(n):
    answer = 0
    for i in range(2, n+1):
        if isPrime(i):
            answer += 1
    return answer

def isPrime(n):
    if n == 2:
        return True
    for i in range(n // 2):
        if n % i 