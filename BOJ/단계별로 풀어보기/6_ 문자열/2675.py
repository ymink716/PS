for _ in range(int(input())):
    r, s = input().split()
    r = int(r)
    result = ""
    for i in s:
        result += i * r
    print(result)