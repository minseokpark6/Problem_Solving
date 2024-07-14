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