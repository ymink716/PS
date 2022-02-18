a, b = input().split()

for i in range(1, 4):
    if int(a[-i]) > int(b[-i]):
        print(a[::-1])
        break
    elif int(a[-i]) < int(b[-i]):
        print(b[::-1])
        break