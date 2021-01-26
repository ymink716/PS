def find_dn(n):
    result = n
    for i in str(n):
        result += int(i)
    return result

array = [1 for _ in range(10001)]

for i in range(10001):
    try:
        array[find_dn(i)] = 0
    except:
        continue

for j in range(1, len(array)):
    if array[j] == 1:
        print(j)