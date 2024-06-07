a, b = map(int, input().split())

if a < b:
    a, b = b, a

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcd(a, b):
    return a * b // gcd(a, b)


print(lcd(a, b))