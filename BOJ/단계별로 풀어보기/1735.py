def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcd(a, b):
    return a * b // gcd(a, b)


a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

a3 = a1 * b2 + a2 * b1
b3 = b1 * b2

gcd = gcd(a3, b3)

print(a3 // gcd, b3 // gcd)
