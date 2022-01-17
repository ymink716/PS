from itertools import permutations

def solution(expression):
    op = [x for x in expression if x in ["+", "-", "*"]]
    nums = list(map(int, expression.replace('+', ' ').replace('-', ' ').replace('*', ' ').split(' ')))

    answer = 0
    s = set(op)
    for p in permutations(s, len(s)):
        for o in p:
            for i in range(len(op)):
                if op[i] == o:
                    nums[i]





# test
print(solution("100-200*300-500+20"))
#print(solution("50*6-3*2"))