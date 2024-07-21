def solution(num, total):
    answer = []
    if num % 2 != 0 :
        center = total // num
        p = num // 2
        for i in range(center-p, center+p+1):
            answer.append(i)
    else:
        l = (num // 2) - 1
        r = (num // 2) + 1
        center = total // num
        for i in range(center-l, center+r):
            answer.append(i)
        
    return answer


'''
4  18    [3,4,5,6]


6  21    [1,2,3,4,5,6]
'''