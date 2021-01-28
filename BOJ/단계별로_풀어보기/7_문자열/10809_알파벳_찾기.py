s = input()
alphabets = 'abcdefghijklmnopqrstuvwxyz'
result = [-1 for _ in range(len(alphabets))]

for i in range(len(s)):
    n = alphabets.find(s[i])  # 알파벳 순서의 위치
    if result[n] == -1:  # 아직 등장하지 않은 값이면 그 자리에 값을 변경
        result[n] = i

for j in result:
    print(j, end=' ')