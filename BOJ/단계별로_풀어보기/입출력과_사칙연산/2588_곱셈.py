a = int(input())
b = input()

n3 = a * int(b[-1])
n4 = a * int(b[-2])
n5 = a * int(b[-3])
n6 = n3 + n4 * 10 + n5 * 100

print(n3)
print(n4)
print(n5)
print(n6)
