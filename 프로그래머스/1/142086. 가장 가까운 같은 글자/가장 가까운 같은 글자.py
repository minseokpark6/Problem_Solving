
def solution(s):
    # 변수 설정 
    answer = []
    last_index = {}
    
    # 문자열 위치 찾기 
    for idx, i in enumerate(s):
        answer.append(idx-last_index[i] if i in last_index else -1)
        last_index[i] = idx
        
    return answer

'''
(1) if - else 문 구조 단순화 
(2) 중복되는 딕셔너리 추가 부문 하나로 합침

## 기존 코드 

def solution(s):
    # 변수 정의 
    answer = []
    dic = {}

    # 문자열 위 찾기 
    for idx, i in enumerate(s):
        if i in dic.keys():
            answer.append(idx - dic[i])
            dic[i] = idx
        else:
            answer.append(-1)
            dic[i] = idx

    # 출력
    return answer
'''