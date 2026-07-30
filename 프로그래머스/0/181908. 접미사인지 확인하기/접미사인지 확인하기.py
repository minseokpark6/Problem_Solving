def solution(my_string, is_suffix):
    # 문자열에 대한 접미사 배열 생성
    suffix = [my_string[i:] for i in range(len(my_string))]
    # 출력
    return 1 if is_suffix in suffix else 0
    
'''
def solution(my_string, is_suffix):
    suffix = [my_string[i:] for i in range(len(my_string))]
    if is_suffix in suffix:
        return 1
    else:
        return 0
'''