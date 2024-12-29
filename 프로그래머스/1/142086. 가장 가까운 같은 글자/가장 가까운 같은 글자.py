def solution(s):
    # 변수 설정
    answer = []
    dic = {}
    
    # 문자열 위치 찾기 
    idx = 0
    for i in s:
        if i in dic.keys():
            answer.append(idx - dic[i])
            dic[i] = idx
            idx += 1
        else:
            answer.append(-1)
            dic[i] = idx
            idx += 1
            
    # 출력
    return answer