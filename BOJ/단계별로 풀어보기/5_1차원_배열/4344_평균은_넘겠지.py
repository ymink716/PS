for _ in range(int(input())):
    data = list(map(int, input().split()))
    avg = sum(data[1:]) / data[0]
    count = 0
    for s in data[1:]:
        if s > avg:
            count += 1
    print("{0:.3f}%".format((count / data[0]) * 100, 3))