def solution(i, j, k):
    # 변수 정의
    target = str(k)
    
    # 출력
    return sum(str(n).count(target) for n in range(i, j+1))


'''
def solution(i, j, k):
    answer = 0
    temp = list(range(i, j+1))
    temp = list(map(str, temp))

    for i in temp:
        for j in i:
            if str(k) in j:
                answer += 1
    return answer
'''