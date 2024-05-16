n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

intersection_length = len(a & b)

print(n - intersection_length + m - intersection_length)