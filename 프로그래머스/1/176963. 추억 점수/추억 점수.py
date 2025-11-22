def solution(name, yearning, photo):
    # 변수 정의 
    dic = {n:y for n, y in zip(name, yearning)}
    
    # 출력 
    return [sum(dic[n] for n in p if n in dic) for p in photo]

'''

## 기존 코드 

def solution(name, yearning, photo):
    # 변수 정의 
    result = []
    dic= {n:y for n, y in zip(name, yearning)}
    
    # 추억 점수 카운트 
    for p in photo:
        score = 0
        for n in p:
            if n in name:
                score += dic[n]
        
        result.append(score)
    
    # 출력
    return result
'''