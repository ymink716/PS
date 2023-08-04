# Strfry
# https://www.acmicpc.net/problem/11328

for _ in range(int(input())):
    a, b = input().split()

    a = str(sorted(list(a)))
    b = str(sorted(list(b)))

    if a == b:
        print("Possible")
    else:
        print("Impossible")