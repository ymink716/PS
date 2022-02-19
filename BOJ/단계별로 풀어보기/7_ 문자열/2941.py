s = input()

count = 0
i = 0
while i < len(s):
    if s[i:i+2] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
        i += 1
    elif s[i:i+3] == 'dz=':
        i += 2
    i += 1
    count += 1

print(count)
