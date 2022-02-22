def solution(dirs):
    x, y = 0, 0
    loads = set()

    for d in dirs:
        nx, ny = x, y
        if d == "U": ny += 1
        elif d == "D": ny -= 1
        elif d == "R": nx += 1
        elif d == "L": nx -= 1

        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue

        # a -> b 와 b -> a 를 하나로 취급하기 위해 둘 다 경로에 추가한 후 마지막에 나누기 2
        loads.add((x, y, nx, ny))
        loads.add((nx, ny, x, y))
        x, y = nx, ny

    return len(loads) // 2


# test case
print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
print(solution("LRLRL"))
