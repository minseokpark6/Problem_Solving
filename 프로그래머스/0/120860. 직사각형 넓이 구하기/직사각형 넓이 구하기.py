def solution(dots):
    x_list = []
    y_list = []
    
    for i in range(4):
        x_list.append(dots[i][0])
        y_list.append(dots[i][1])

    x_list = sorted(list(set(x_list)))
    y_list = sorted(list(set(y_list)))

    x = x_list[1] - x_list[0]
    y = y_list[1] - y_list[0]

    answer = x*y
    
    return answer