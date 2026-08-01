def solution(my_string):
    return sorted(int(n) for n in my_string if n.isdigit())

'''
def solution(my_string):
    answer = sorted([int(num) for num in my_string if num.isdigit()])
    return answer

'''
