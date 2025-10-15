def solution(s): 
    # 변수 지정 
    cnt, zero_cnt = 0, 0 

    # 이진변환 
    while s != "1":
        # 제거한 0의 개수와 횟수 더하기
        zero_cnt += s.count("0")
        cnt += 1
        
        # s에서 0 제거
        s = format(s.count("1"), "b")
        
    # 출력 
    return [cnt, zero_cnt]


'''
## 이전 코드

def solution(s):
    # 변수 및 리스트 설정
    answer = []
    c, z = 0, 0
    
    # 이진 변환 
    while True:
        # 제거할 0의 개수와 회차 더하기
        z += s.count("0")
        c += 1

        # 0 제거 후 길이(l) 및 이진 변환 결과값 변수 s에 다시 저장
        l = len("".join([i for i in s if i == "1"]))
        s = format(l, "b")
        
        if s == "1":
            break

    # 리스트에 제거한 0의 개수 및 회차 수 담기 
    answer.append(c)
    answer.append(z)
    
    # 출력
    return answer
'''