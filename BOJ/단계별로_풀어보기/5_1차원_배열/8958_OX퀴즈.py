t = int(input())
for _ in range(t):
    data = input()
    count = 1
    result = 0
    if data[0] == 'O':
        result += 1
    for i in range(1, len(data)):
        if data[i] == 'O':
            if data[i - 1] == data[i]:
                count += 1
            result += count
        else:
            count = 1
    print(result)
