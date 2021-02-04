n = int(input())

answer = 666
count = 1
while count != n:
    answer += 1
    if str(answer).find("666") != -1:
        count += 1

print(answer)