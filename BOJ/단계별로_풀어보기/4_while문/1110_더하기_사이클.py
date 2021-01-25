n = int(input())

count = 0
now = str(n)
while True:
    if len(now) == 1:
        now = "0" + now
    temp = int(now[0]) + int(now[1])
    now = now[-1] + str(temp)[-1]
    count += 1
    if n == int(now):
        break

print(count)