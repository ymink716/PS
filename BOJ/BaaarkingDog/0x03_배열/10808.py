# 알파벳 개수
# https://www.acmicpc.net/problem/10808

s = input()
array = [0] * 26

for i in s:
    array[ord(i) - ord('a')] += 1

print(*array)