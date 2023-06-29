# 서로 다른 부분 문자열의 개수
# https://www.acmicpc.net/problem/11478

s = input()

result = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        result.add(s[i:j + 1])

print(len(result))