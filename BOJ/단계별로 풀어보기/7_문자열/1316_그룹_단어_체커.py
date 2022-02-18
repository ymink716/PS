count = 0
for _ in range(int(input())):
    s = input()
    count += 1
    check_list = [0 for _ in range(26)]
    prev = s[0]
    for i in s:
        # 현재 문자가 이미 나온 문자이고, 이전 문자의 값과 다르면 연속이 아님
        if check_list[ord(i) - ord('a')] > 0 and prev != i:
            count -= 1
            break
        check_list[ord(i) - ord('a')] += 1
        prev = i
print(count)