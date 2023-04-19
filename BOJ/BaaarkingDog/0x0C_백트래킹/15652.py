# N과 M (4)

from itertools import combinations_with_replacement

n, m = map(int, input().split())
array = [i for i in range(1, n + 1)]

for l in combinations_with_replacement(array, m):  # 중복을 허용하는 조합
    print(*l)