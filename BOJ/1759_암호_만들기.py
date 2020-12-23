import itertools

l, c = map(int, input().split())
array = input().split()
array.sort()


for key in itertools.combinations(array, l):
    m = 0
    for i in key:
        if i in ['a', 'e', 'i', 'o', 'u']:
            m += 1
    if m >= 1 and l - m >= 2:
        print(''.join(list(key)))

"""
4 6
a t c i s w
"""