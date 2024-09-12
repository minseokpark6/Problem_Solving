def solution(phone_number):
    hidden = "*" * (len(phone_number) - 4)
    answer = hidden + phone_number[-4:]
    return answer