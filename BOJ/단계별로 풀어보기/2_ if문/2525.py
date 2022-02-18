h, m = map(int, input().split())
need = int(input())

a, b = divmod(need, 60)
h += a
m += b

if m >= 60:
    m -= 60
    h += 1

if h >= 24:
    h -= 24

print(h, m)