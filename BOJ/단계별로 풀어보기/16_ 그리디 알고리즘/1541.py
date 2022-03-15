data = input().split('-')

answer = 0
for n in data[0].split('+'):
    answer += int(n)

for i in range(1, len(data)):
    total = 0
    for n in data[i].split('+'):
        total += int(n)
    answer -= total

print(answer)