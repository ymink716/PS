# 비밀지도 (못품)
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        print(str(bin(arr1[i] | arr2[i]))[2:])
        answer.append(str(bin(arr1[i] | arr2[i]))[2:].replace('1', '#').replace('0', ' '))
    return answer  
        


# 테스트
#print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))