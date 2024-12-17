def solution(dartResult):
    # 변수 정의
    scores = [str(i) for i in range(11)]
    answer = []
    
    # 점수 합산
    for i in dartResult:
        if i in scores:
            # 10의 경우 추가
            if answer and answer[-1] == 1 and i == "0":
                answer[-1] = int(str(answer[-1]) + i)
            # 그 외 정수
            else:
                answer.append(int(i))
        # 싱글은 굳이 넣을 필요 없음
        elif i in ["D", "T"]:
            answer[-1] **= 2 if i == "D" else 3
        elif i == "*":
            answer[-1] *= 2
            if len(answer) >= 2:
                answer[-2] *= 2
        elif i == "#":
            answer[-1] = -(answer[-1])
    # 출력
    return sum(answer)




""" 
## try 1
## 오답 >> 숫자 10 처리가 안됨 

def solution(dartResult):
    # 변수 정의
    scores = [str(i) for i in range(11)]
    answer = []
    
    # 점수 합산
    for i in dartResult:
        if i in scores:
            answer.append(int(i))
        elif i in ["D", "T"]:
            answer[-1] **= 2 if i == "D" else 3
        elif i == "*":
            answer[-1] *= 2
            if len(answer) >= 2:
                answer[-2] *= 2
        elif i == "#":
            answer[-1] = -(answer[-1])

    # 출력
    return sum(answer)
"""
