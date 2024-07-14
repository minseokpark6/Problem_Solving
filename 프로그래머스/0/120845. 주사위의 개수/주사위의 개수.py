def solution(box, n):
    answer = 0
    a = box[0] // n
    answer += a

    b = box[1] // n
    answer *= b

    c = box[2] // n
    answer *= c

    return answer