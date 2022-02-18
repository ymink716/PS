n = input()

data = []
for i in n:
    data.append(int(i))
data.sort(reverse=True)

for i in data:
    print(i, end="")