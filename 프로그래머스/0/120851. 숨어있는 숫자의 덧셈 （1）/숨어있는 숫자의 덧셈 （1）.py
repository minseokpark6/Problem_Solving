def solution(my_string):
    # 문자열에서 숫자 골라내기
    num_list = [int(ch) for ch in my_string if ch.isdigit()]
    # 출력
    return sum(num_list)

'''
def solution(my_string):
    # 초기화
    answer = 0
    # my_string에서 숫자만 추출(숫자도 타입은 str)
    num_list = [char for char in my_string if char.isdigit()]
    for num in num_list:
        num = int(num)
        answer += num
    return answer
'''