def solution(brown, yellow):
    # 빈 리스트 생성
    answer = []
    # a와 b값 찾기 >> a(가로)의 길이는 brown 수의 반보다 작을 수 밖에 없음 
    for i in range(3, brown//2):
        a, b = i, ((brown+4)/2) - i
        if a * b == brown + yellow and (a >= b):
            answer.append(a)
            answer.append(b)
    # 출력
    return answer


"""
return = [a, b]

(1)
a, b는 brown + yellow의 약수로 이루어져 있음
brown + yellow = a * b


(2)
brown은 1줄로 이루어진 테두리이기 때문에
(b-2)가 yellow의 세로줄 수 

(3)
brown = (b-2)*2 + (a-2)*2 + 4 = 2 * (a+b) - 4
a + b = (brown + 4) / 2
b = (brown + 4) / 2 - a

"""