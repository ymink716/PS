def solution(phone_book):
    d = {}

    # 등장한 전화번호들을 딕셔너리로
    for phone_number in phone_book:
        d[phone_number] = 1

    # 전화번호들을 순회하면서
    for phone_number in phone_book:
        temp = ""
        # 전화번호의 숫자 하나하나를 순회하면서
        for number in phone_number:
            temp += number
            # 딕셔너리 키로 같은 전화번호가 있지만 전체 번호는 다른 경우
            # 해당 번호(phone_number)가 다른 번호를 접두어로 포함
            # (리스트로 탐색하는 경우보다 딕셔너리를 탐색하는 것이 복잡도가 줄어든다.)
            if temp in d and temp != phone_number:
                return False
    return True


# test case
pb1 = ["119", "97674223", "1195524421"]
pb2 = ["123", "456", "789"]
pb3 = ["12", "123", "1235", "567", "88"]

print(solution(pb1))
print(solution(pb2))
print(solution(pb3))