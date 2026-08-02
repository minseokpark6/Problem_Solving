def solution(order):
    # 변수 정의
    clap = ['3', '6', '9']
    
    # 출력
    return sum(1 for i in str(order) if i in clap)


'''
def solution(order):
    answer = 0
    order = str(order)

    n3 = order.count('3')
    answer += n3
    n6 = order.count('6')
    answer += n6
    n9 = order.count('9')
    answer += n9
    return answer
'''