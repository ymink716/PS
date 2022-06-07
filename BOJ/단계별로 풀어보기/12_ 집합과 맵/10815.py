n = int(input())
d = dict()

for a in map(int, input().split()):
    d[a] = 1

m = int(input())
answer = ""
for b in map(int, input().split()):
    if d.get(b):
        answer += "1 "
    else:
        answer += "0 "

print(answer)