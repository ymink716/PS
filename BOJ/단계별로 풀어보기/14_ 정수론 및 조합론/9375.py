for _ in range(int(input())):
    d = dict()
    for _ in range(int(input())):
        name, category = input().split()
        try:
            d[category].append(name)
        except KeyError:
            d[category] = [name]

    result = 1
    for key in d.keys():
        result = result * (len(d[key]) + 1)
    print(result - 1)