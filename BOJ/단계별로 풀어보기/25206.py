credit = 0
total = 0

for _ in range(20):
    _, c, g = input().split()

    if g == 'A+':
        g = 4.5
    elif g == 'A0':
        g = 4.0
    elif g == 'B+':
        g = 3.5
    elif g == 'B0':
        g = 3.0
    elif g == 'C+':
        g = 2.5
    elif g == 'C0':
        g = 2.0
    elif g == 'D+':
        g = 1.5
    elif g == 'D0':
        g = 1.0
    elif g == 'F':
        g = 0.0
    elif g == 'P':
        continue

    credit += float(c)
    total += float(c) * g

print(total / credit)