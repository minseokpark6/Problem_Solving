def solution(answers):
    # 변수 지정
    patterns = [
        [1, 2, 3, 4, 5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]

    result = [0, 0, 0]
    
    # 정답 개수 카운트 
    for idx, answer in enumerate(answers):
        for i, pattern in enumerate(patterns):
            if answer == pattern[idx % len(pattern)]:
                result[i] += 1
    
    # 출력
    max_score = max(result)
    return [i+1 for i, s in enumerate(result) if s == max_score]

'''
# 개선점
(1) 기존 통과 코드에서 불필요한 루프를 -> pattern[idx % len(pattern)]로 대체 


## 기존 통과 코드 

def solution(answers):
    # 변수 지정
    circle = (len(answers)//5)+1
    supo_1 = [1,2,3,4,5] * circle
    supo_2 = [2,1,2,3,2,4,2,5] * circle
    supo_3 = [3,3,1,1,2,2,4,4,5,5] * circle
    
    # 정답 카운트 
    result = []
    c1, c2, c3 = 0, 0, 0
    for idx in range(len(answers)):
        if answers[idx] == supo_1[idx]:
            c1 += 1
        if answers[idx] == supo_2[idx]:
            c2 += 1
        if answers[idx] == supo_3[idx]:
            c3 += 1
    result.extend([c1, c2, c3])
    
    # 출력
    return [i+1 for i, c in enumerate(result) if c == max(result)]
    
'''