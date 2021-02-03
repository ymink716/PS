n = int(input())

if n == 1:
    print(1)
else:
    step = 6
    prev = 1
    passed = 1
    while True:
        now = prev + step
        passed += 1
        if prev <= n <= now:
            print(passed)
            break
        prev += step
        step += 6
