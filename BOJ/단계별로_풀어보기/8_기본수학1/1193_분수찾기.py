x = int(input())

line = 0
while x > line:
    x -= line
    line += 1

a, b = 0, 0
if line % 2 == 1:
    a = line - (x - 1)
    b = x
else:
    a = x
    b = line - (x - 1)

print("{0}/{1}".format(a, b))