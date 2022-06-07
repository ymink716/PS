import math

n = int(input())
nums = list(map(int, input().split()))
a, b, c, d = map(int, input().split())
max_num, min_num = -math.inf, math.inf

def solution(num, idx, add, sub, mul, div):
    global max_num, min_num
    if idx == n:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return

    if add > 0:
        solution(num + nums[idx], idx + 1, add - 1, sub, mul, div)
    if sub > 0:
        solution(num - nums[idx], idx + 1, add, sub - 1, mul, div)
    if mul > 0:
        solution(num * nums[idx], idx + 1, add, sub, mul - 1, div)
    if div > 0:
        solution(int(num / nums[idx]), idx + 1, add, sub, mul, div - 1)


solution(nums[0], 1, a, b, c, d)
print(max_num)
print(min_num)
