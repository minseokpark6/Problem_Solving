from math import prod

def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        return prod(num_list)

'''
# list 누적곱

math 라이브러리의 prod 사용
'''