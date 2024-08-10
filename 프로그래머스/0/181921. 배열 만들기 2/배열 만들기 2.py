def solution(l, r):
    answer = []
    num_list = [num for num in range(l, r+1)]
    a = ["0", "5"]
    for num in num_list:
        Bol = True
        str_num = str(num)
        for s in str_num:
            if s not in a:
                Bol = False
        if Bol == True:
            answer.append(num)
    if len(answer) == 0:
        answer.append(-1)
    return answer