def solution(num_list):
    # 변수 정의 
    a, b = num_list[-1], num_list[-2]
    # num_list 원소 추가 
    if a > b:
        num_list.append(a-b)
    else:
        num_list.append(a*2)
    # 출력
    return num_list

'''
def solution(num_list):
    if num_list[-1] > num_list[-2]:
        a = num_list[-1] - num_list[-2]
    else:
        a = num_list[-1] * 2
    num_list.append(a)
    return num_list
'''