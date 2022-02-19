s = input().upper()

result = dict()
for i in s:
    if i not in result:
        result[i] = 0
    result[i] += 1

max_value = 0
answer = ""
same = False
for k in result:
    if result[k] > max_value:
        answer = k
        max_value = result[k]
        same = False
    elif result[k] == max_value:
        same = True

if same:
    print("?")
else:
    print(answer)


