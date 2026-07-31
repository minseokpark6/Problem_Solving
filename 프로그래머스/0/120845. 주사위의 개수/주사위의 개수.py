def solution(box, n):
    # 변수정의
    cnt = 0
    # 주사위 최대 개수 구하기
    for l in box:
        if cnt == 0:
            cnt = (l//n)
        else:
            cnt *= (l//n)
    # 출력
    return cnt


'''
def solution(box, n):
    answer = 0
    a = box[0] // n
    answer += a

    b = box[1] // n
    answer *= b

    c = box[2] // n
    answer *= c

    return answer


'''
def solution(box, n):
    answer = 0
    a = box[0] // n
    answer += a

    b = box[1] // n
    answer *= b

    c = box[2] // n
    answer *= c

    return answer
'''
'''


'''
def solution(box, n):
    answer = 0
    a = box[0] // n
    answer += a

    b = box[1] // n
    answer *= b

    c = box[2] // n
    answer *= c

    return answer
'''