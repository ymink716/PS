# 잃어버린 괄호
# https://www.acmicpc.net/problem/1541

data = input().split('-')  # - 기준으로 스플릿

answer = 0
# 0번째에 오는 숫자들은 - 가 나오기 전의 숫자들이므로 모두 더해줌
for n in data[0].split('+'):
    answer += int(n)

# 이후 숫자들은 괄호로 묶여 - 이므르 모두 빼줌
for i in range(1, len(data)):
    for n in data[i].split('+'):
        answer -= int(n)

print(answer)