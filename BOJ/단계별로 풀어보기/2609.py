a, b = map(int, input().split())

gcd = 1
for i in range(min(a, b), 1, -1):
    if a % i == 0 and b % i == 0:
        gcd = i
        break
lcm = gcd * (a // gcd) * (b // gcd)

print(gcd)
print(lcm)