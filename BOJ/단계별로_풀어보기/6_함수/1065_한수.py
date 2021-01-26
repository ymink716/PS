def check(x):
    x = str(x)
    if int(x[0]) - int(x[1]) == int(x[1]) - int(x[2]):
        return True
    return False

n = int(input())

result = 0
if len(str(n)) >= 3:
    result += 99
    for x in range(100, n + 1):
        if check(x):
            result += 1
else:
    result = n

print(result)