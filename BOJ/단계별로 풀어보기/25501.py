def recursion(s, l, r, cnt):
    if l >= r: return [1, cnt+1]
    elif s[l] != s[r]: return [0, cnt+1]
    else: return recursion(s, l+1, r-1, cnt+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0)

for _ in range(int(input())):
    s = input()
    result = isPalindrome(s)
    print(result[0], result[1])