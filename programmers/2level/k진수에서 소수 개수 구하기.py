import math

# 진법 변환
def convert_num(n, k):
    base = ""
    while n > 0:
        n, mod = divmod(n, k)
        base += str(mod)
    num_k = base[::-1]
    return str(num_k)

# 소수 판별
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    converted = convert_num(n, k)
    nums = converted.split('0')  # 0을 기준으로 split하면 검사해야할 숫자들만 나옴

    answer = 0
    for i in range(len(nums)):
        try:
            if is_prime(int(nums[i])):
                answer += 1
        except ValueError:
            continue
    return answer


# test
print(solution(437674, 3))
print(solution(110011, 10))