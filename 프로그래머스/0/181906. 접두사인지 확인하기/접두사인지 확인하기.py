def solution(my_string, is_prefix):
    # 접두사 리스트 정의 
    arr = [my_string[:idx] for idx in range(1, len(my_string)+1)]
    # 출력
    return 1 if is_prefix in arr else 0

'''
def solution(my_string, is_prefix):
    prefix_list = []
    for i in range(len(my_string)):
        prefix_list.append(my_string[:i])
    if is_prefix in prefix_list:
        return 1
    else:
        return 0
'''